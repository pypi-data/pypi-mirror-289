#  This code is part of cqlib.
#  #
#  (C) Copyright qc.zdxlz.com 2024.
#  #
#  This code is licensed under the Apache License, Version 2.0. You may
#  obtain a copy of this license in the LICENSE.txt file in the root directory
#  of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#  #
#  Any modifications or derivative works of this code must retain this
#  copyright notice, and modified files need to carry a notice indicating
#  that they have been altered from the originals.
#
from typing import List, Union, Tuple, Optional
from numbers import Number
import pandas as pd
from functools import singledispatch
from collections.abc import Sequence, MutableSequence
from .exceptions import CqlibQcisCircuitError
from .base import QcisQubit, QcisTime, QcisAngle, QcisParams


@singledispatch
def qubit_idx_validator(obj):
    """
    validate if string could be parsed as qubit and return parsed qubit idx.

    Args:
        q (str|int): . e.g.: Q10 | 2

    Raises:
        CqlibQcisCircuitError: raise if input string could not be parsed as qubit.

    Returns:
        QcisQubit: An instance of class QcisQubit which records qubit idx.
    """
    raise TypeError(f'For qubit idx validator, input {type(obj)} is not valid.')


@qubit_idx_validator.register(str)
def _(q: str):
    """
    Input parameter as string.
    """
    # check if startswith Q
    if not q.startswith('Q'):
        raise CqlibQcisCircuitError(f'{q} is not a valid qubit cause it does not start with Q`')
    # check if startswith Q
    if not q[1:].isdigit():
        raise CqlibQcisCircuitError(f'{q} is not a valid qubit cause {q}[1:] is not digit')
    # validate qubit range
    q_id = int(q[1:])
    return QcisQubit(q_id)


@qubit_idx_validator.register(int)
def _(q: int):
    """
    Input parameter as integer.
    """
    return QcisQubit(q)


def qcis_angle_validator(angle: str):
    """
    check if string could be parsed as qcis angle and return parsed angle.
    
    Args:
        angle: str. Transform to float type.

    Raises:
        CqlibQcisCircuitError: raise if input string could not be parsed as float angle.

    Returns:
        QcisAngle: An instance of class QcisAngle which records angle.
    """
    try:
        return QcisAngle(float(angle))
    except ValueError:
        raise CqlibQcisCircuitError(f'{angle} is not a valid float number.')


def qcis_time_validator(t: str):
    """
    check if string could be parsed as time(int) and return parsed time.
    unit is 0.5 ns
    
    Args: 
        t: str. One time step.
        
    Raises:
        CqlibQcisCircuitError: if t couldn't be transformed into integer.\
    
    Returns:
        QcisTime: An instance of class QcisTime.
    """
    try:
        return QcisTime(int(t))
    except ValueError:
        raise CqlibQcisCircuitError(f'{t} is not a valid integer number.')


def qubit_list_repeat_validator(input_qubits):
    """
    check if qubit list has repeated qubit index.
    
    Args:
        *input_qubits: all packed input qubits.
        
    Raises:
        CqlibQcisCircuitError: raise if there exists repeated qubit index.

    """

    if len(input_qubits) > len(set(input_qubits)):
        raise CqlibQcisCircuitError(f'Qubit input {input_qubits} has repeated qubit index')


gate_validate_rule_dict = {
    # Define validate rules based on gate name including native gate and compound gate.

    # native gate
    'X2P': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,)
    },
    'X2M': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,)
    },
    'Y2P': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,)
    },
    'Y2M': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,)
    },
    'CZ': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator, qubit_idx_validator),
        'conjunct_validator': (qubit_list_repeat_validator,)
    },

    'RZ': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,),
        'para_validator': (qcis_angle_validator,),
    },
    'I': {
        'class': 'native',
        'qubit_validator': (qubit_idx_validator,),
        'para_validator': (qcis_time_validator,),
    },
    'B': {
        'class': 'native',
        'qubit_validator': [qubit_idx_validator],
        'conjunct_validator': (qubit_list_repeat_validator,)
    },
    'M': {
        'class': 'native',
        'qubit_validator': [qubit_idx_validator],
        'conjunct_validator': (qubit_list_repeat_validator,)
    },

    # compound gate
    'X': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'Y': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'Z': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'H': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'S': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'T': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'TD': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,)
    },
    'RX': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,),
        'para_validator': (qcis_angle_validator,),
    },
    'RY': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,),
        'para_validator': (qcis_angle_validator,),
    },
    'RXY': {
        'class': 'compound',
        'qubit_validator': (qubit_idx_validator,),
        'para_validator': (qcis_angle_validator, qcis_angle_validator),
    }
}


def _format_validator_input_num(value):
    """
    output validator number based on input value.
    """
    if isinstance(value, MutableSequence):
        return 'many'
    elif isinstance(value, Sequence):
        return len(value)
    else:
        return '/'


def valid_operation():
    """
    output formatted operation name, class and its qubit/parameter inputs number.

    Returns:
        pd.DataFrame: formatted operation tables.
    """
    df_ori = pd.DataFrame.from_dict(gate_validate_rule_dict, orient='index')
    df_new = df_ori[['class']]
    df_new['qubit_input_num'] = df_ori['qubit_validator'].apply(_format_validator_input_num)
    df_new['param_input_num'] = df_ori['para_validator'].apply(_format_validator_input_num)
    return df_new


def validate_gate_name_and_get_rule(gate_name: str):
    """
    validate gate name is accepted by cqlib

    Args:
        gate_name (str): input gate name

    Returns:
        rules (tuple): three kinds of rules stored inside gate_validate_rule_dict

    Raises:
        KeyError: if gate name not in gate_validate_rule_dict

    """
    if gate_name not in gate_validate_rule_dict:
        raise KeyError(f'{gate_name} is not a valid gate name or not accepted by cqlib')
    qubit_valid_rule = gate_validate_rule_dict[gate_name].get('qubit_validator')
    param_valid_rule = gate_validate_rule_dict[gate_name].get('para_validator', None)
    conjunct_valid_rule = gate_validate_rule_dict[gate_name].get('conjunct_validator', None)
    return qubit_valid_rule, param_valid_rule, conjunct_valid_rule


def validate_qcis_order(gate_name: str, params: Sequence):
    """
    check if gate_name could be parsed as valid gate name and
    check if para_num is matched with validators.

    Instruction Checker
    divided into three parts:
    1. Para number length check:
        check if input parameter numbers is matched with validators if rule is defined as tuple.
        Skip this part if rule is defined as list.
    2. Validate each parameter given rule:
        Rules are defined as sequence of funcs. Try to call func with each parameter as input.
    3. Check conjunction rule:
        If there exists conjunction validator between parameters, call conjunction validating func to check if input
        parameters matched with rules.

    Args:
        gate_name: str. e.g.: H. Should be defined inside gate_validate_rule dict.
        params: Sequence. List of parameters.

    Raises:
        KeyError: raise if gate name not defined in gate_validate_rule_dict.
        CqlibQcisCircuitError: if gate_name could not be parsed as valid gate name or
            para_num is not matched with validators.

    Returns:
        List[Union[QcisQubit, QcisTime, QcisAngle]]: A list of parsed object from qcis order.
    """
    qubit_list = []
    params_list = []

    qubit_valid_rule, param_valid_rule, conjunct_valid_rule = validate_gate_name_and_get_rule(gate_name)

    rule_list = list(qubit_valid_rule)
    if param_valid_rule:
        rule_list.extend(list(param_valid_rule))
    # 1. para number length check
    if isinstance(qubit_valid_rule, MutableSequence):
        rule_list = [qubit_valid_rule[0]] * len(params)
    elif isinstance(qubit_valid_rule, tuple):
        if len(params) != len(rule_list):
            raise CqlibQcisCircuitError(f'{gate_name} requires {len(rule_list)} inputs but '
                                         f'{len(params)} is given')
    # 2. check each parameter with its given rule
    for i, param in enumerate(params):
        para_format = rule_list[i](param)
        if isinstance(para_format, QcisQubit):
            qubit_list.append(para_format)
        if isinstance(para_format, QcisParams):
            params_list.append(para_format)
    # 3. check conjunction rule
    if conjunct_valid_rule:
        for conjunct_rule in conjunct_valid_rule:
            conjunct_rule(params)
    return tuple(qubit_list), tuple(params_list)


def validate_instruction_input(gate_name: str, qubits_index: Tuple[int], params: Optional[Tuple[Number]]):
    """
    check if input parameters to construct instruction are valid.

    Args:
        gate_name (str): input gate name
        qubits_index (Tuple[int]): a tuple of integer indicates qubit index
        params (Optional[Tuple[Number]]): a tuple of numbers indicates operation's parameter

    Returns:
    """
    qubit_valid_rule, param_valid_rule, conjunct_valid_rule = validate_gate_name_and_get_rule(gate_name)
    if isinstance(qubit_valid_rule, MutableSequence):
        for qubit_idx in qubits_index:
            qubit_valid_rule[0](qubit_idx)
    else:
        # check qubits
        if len(qubits_index) != len(qubit_valid_rule):
            raise CqlibQcisCircuitError(f'{gate_name} requires {len(qubit_valid_rule)} qubit index but '
                                         f'{len(qubits_index)} is given')
        for i, qubit_idx in enumerate(qubits_index):
            qubit_valid_rule[i](qubit_idx)
    # check params
    if params:
        if param_valid_rule is None:
            raise CqlibQcisCircuitError(f'{gate_name} requires no parameters but '
                                         f'{len(params)} is given')
        if len(params) != len(param_valid_rule):
            raise CqlibQcisCircuitError(f'{gate_name} requires {len(param_valid_rule)} parameters but '
                                         f'{len(params)} is given')
        for i, param in enumerate(params):
            param_valid_rule[i](param)
    else:
        if param_valid_rule:
            raise CqlibQcisCircuitError(f'{gate_name} requires {len(param_valid_rule)} parameters but '
                                         f'None is given')
    # check conjunction rule
    if conjunct_valid_rule:
        temp_params = list(qubits_index)
        if params:
            temp_params.extend(list(params))
        for conjunct_rule in conjunct_valid_rule:
            conjunct_rule(temp_params)
