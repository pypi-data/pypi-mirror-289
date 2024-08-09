from typing import Union, Sequence, Optional, Tuple
from numbers import Number
from .instruction_validator import validate_qcis_order, validate_instruction_input, valid_operation
from .base import QcisQubit, QcisParams


class QcisInstruction:
    def __init__(self, operation: str, qubits_idx: Union[Sequence[int], Sequence[QcisQubit], QcisQubit, int],
                 params: Optional[Union[Sequence[Number], Sequence[QcisParams], QcisParams, Number]] = None):
        """
        Initialize QcisInstruction.

        Args:
            operation: str
            qubits_idx: Union[Sequence[int], Sequence[QcisQubit], QcisQubit, int]
            params: Optional[Union[Sequence, QcisParams]]

        """
        operation = operation.upper()
        qubits_idx_temp = self.validate_qubits_idx(qubits_idx)
        params_temp = self.validate_params(params)
        self.check_modified(operation, qubits_idx_temp, params_temp)
        self._operation = operation
        self._qubits_idx = qubits_idx_temp
        self._params = params_temp

    @staticmethod
    def instruction_from_str(qcis_str):
        """

        Args:
            qcis_str (str): qcis string.

        Returns:
            QcisInstruction: an instance of QcisInstruction
        """
        qcis_str_temp = qcis_str.upper().strip(' ').strip('\n').strip(' ')
        if len(qcis_str_temp.split('\n')) > 1:
            raise ValueError('Given multiple lines of qcis order, only one line is allowed.')
        operation, *params = [x for x in qcis_str_temp.split(' ') if x]
        qubit_list, params_list = validate_qcis_order(operation, params)
        return QcisInstruction(operation, qubit_list, params=params_list)

    @staticmethod
    def check_modified(operation: str, qubits_index: Tuple[int], params: Optional[Tuple[Number]]):
        """

        Args:
            operation (str): operation name.
            qubits_index (Tuple[int]): a tuple of qubits index.
            params (Optional[Tuple[Number]]): a tuple of input parameters.

        Raises:
            CqlibQcisCircuitError: if given invalid inputs, it will throw a CqlibQcisCircuitError.

        """
        validate_instruction_input(operation, qubits_index, params)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        temp_str = self._operation.lower() + ' '
        for q in self._qubits_idx:
            temp_str += f'q{q} '
        if self._params:
            for para in self._params:
                temp_str += f'{para} '
        temp_str = temp_str.rstrip(' ')
        return temp_str

    @staticmethod
    def validate_qubits_idx(qubits_idx):
        """
        validate input qubits index

        Args:
            qubits_idx: Union[Sequence[int], Sequence[QcisQubit], QcisQubit, int]

        Returns:
            Tuple[int]: a tuple of integer which represents qubit index.

        """
        if isinstance(qubits_idx, QcisQubit):
            return tuple([qubits_idx.idx])
        elif isinstance(qubits_idx, int):
            return tuple([qubits_idx])
        elif isinstance(qubits_idx, Sequence):
            temp_idx_list = []
            for q in qubits_idx:
                if isinstance(q, QcisQubit):
                    temp_idx_list.append(q.idx)
                elif isinstance(q, int):
                    temp_idx_list.append(q)
                else:
                    raise TypeError(f'qubits_idx must be int or QcisQubit but {q} of type {type(q)} has given.')
            return tuple(temp_idx_list)
        else:
            raise TypeError(f'Invalid input type of {type(qubits_idx)} for input qubits_idx')

    @staticmethod
    def validate_params(params):
        """
        validate input params

        Args:
            params: Union[Sequence, QcisParams]
        """
        if not params:
            return None
        if isinstance(params, QcisParams):
            return tuple([params.value])
        elif isinstance(params, Number):
            return tuple([params])
        elif isinstance(params, Sequence):
            temp_param_list = []
            for p_temp in params:
                if isinstance(p_temp, QcisParams):
                    temp_param_list.append(p_temp.value)
                elif isinstance(p_temp, Number):
                    temp_param_list.append(p_temp)
                else:
                    raise TypeError(f'qubits_idx must be Number but {p_temp} of type {type(p_temp)} has given.')
            return tuple(temp_param_list)
        else:
            raise TypeError(f'Invalid input type of {type(params)} for input params')

    @staticmethod
    def get_valid_operation():
        return valid_operation()
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation):
        self.check_modified(operation, self._qubits_idx, self._params)
        self._operation = operation

    @property
    def qubits_idx(self):
        return self._qubits_idx

    @qubits_idx.setter
    def qubits_idx(self, qubits_idx):
        qubits_temp = self.validate_qubits_idx(qubits_idx)
        self.check_modified(self.operation, qubits_temp, self._params)
        self._qubits_idx = qubits_temp

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        params_temp = self.validate_params(params)
        self.check_modified(self.operation, self._qubits_idx, params_temp)
        self._params = params_temp
