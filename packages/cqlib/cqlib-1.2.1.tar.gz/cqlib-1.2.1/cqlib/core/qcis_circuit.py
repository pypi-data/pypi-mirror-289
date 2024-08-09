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
from typing import List, Optional, Union
import types
from .qcis_instruction import QcisInstruction
from .instruction_validator import validate_qcis_order, gate_validate_rule_dict


class QcisCircuit:
    """
    Core calib representation of a quantum circuit.
    """

    def __init__(self, instruction_list: Optional[List[QcisInstruction]] = None):
        if instruction_list:
            self.instruction_list = instruction_list
        else:
            self.instruction_list = []

    def __getattribute__(self, item):
        """
        use getattribute to add instruction

        Args:
            item: str

        """
        if item.upper() in gate_validate_rule_dict:
            return types.MethodType(self.add_instruction, item)
        else:
            return super().__getattribute__(item)

    def __repr__(self):
        return self.to_qcis_str(show_row_num=True)

    def __str__(self):
        return self.to_qcis_str()

    def __len__(self):
        return len(self.instruction_list)

    @property
    def q_list(self):
        q_set_temp = set()
        for instruct in self.instruction_list:
            for q_index in instruct.qubits_idx:
                q_set_temp.add(q_index)
        return list(q_set_temp)

    def to_qcis_str(self, show_row_num: bool = False):
        """
        Convert QcisCircuit to qcis string.
        """
        temp_str = ''
        for i, instruct_temp in enumerate(self.instruction_list):
            if show_row_num:
                temp_str += f'{i + 1:>4} '
            temp_str += str(instruct_temp)
            temp_str += '\n'
        temp_str = temp_str.rstrip('\n')
        return temp_str

    def decompose(self):
        """
        Decompose compound gate into native gate
        """
        pass

    def add_instruction(self, instruct: Union[QcisInstruction, str],
                        q_index_list: Optional[Union[List[int], int]] = None,
                        params: Optional[List[float]] = None):
        """
        Args:
            instruct (QcisInstruction): one line of qcis instruction.
            q_index_list (Optional[List[int]]): input q index list.
            params (Optional[List[float]]): input operation parameters.
        """
        self._handle_instruction(instruct, q_index_list, params)

    def insert_instruction(self, line_index: int, instruct: Union[QcisInstruction, str],
                           q_index_list: Optional[Union[List[int], int]] = None,
                           params: Optional[List[float]] = None):
        """
        Insert instruction into circuit given line index.

        Args:
            line_index (int): line index indicates where to insert the instruction.
            instruct (QcisInstruction): one line of qcis instruction.
            q_index_list (Optional[List[int]]): input q index list.
            params (Optional[List[float]]): input operation parameters.

        Raises：
            TypeError: If input instruction is not an instance of QcisInstruction or line index is not a int.
        """
        if not isinstance(line_index, int):
            raise TypeError(f'Input line index must be an integer but {type(line_index)} was given.')
        self._handle_instruction(instruct, q_index_list, params, line_index)

    def _handle_instruction(self, instruct: Union[QcisInstruction, str], q_index_list: Optional[List[int]] = None,
                            params: Optional[List[float]] = None, line_index: Optional[int] = None):

        """
        Handle instructions.
        If line index is not None, insert instruction. Or append instruction.

        """
        if isinstance(instruct, QcisInstruction):
            if line_index:
                self.instruction_list.insert(line_index, instruct)
            else:
                self.instruction_list.append(instruct)
        elif isinstance(instruct, str):
            if q_index_list is None:
                raise ValueError('q_index_list cannot be None when input is a gate name.')
            if line_index:
                self.instruction_list.insert(line_index, QcisInstruction(instruct, q_index_list, params))
            else:
                self.instruction_list.append(QcisInstruction(instruct, q_index_list, params))
        else:
            raise TypeError(f'Invalid input type, expect QcisInstruction or str, got {type(instruct)} instead.')

    @staticmethod
    def circuit_from_qcis_str(qcis_str: str):
        """

        Args:
            qcis_str: input qcis string.

        Returns:
            QcisCircuit: an instance of QcisCircuit parsed from qcis string.
        """
        instruction_list = []
        for line in qcis_str.upper().split('\n'):
            line = line.strip(' ')
            if line:
                operation, *params = [x for x in line.split(' ') if x]
                qubit_list, params_list = validate_qcis_order(operation, params)
                instruction_list.append(QcisInstruction(operation, qubit_list, params=params_list))
        return QcisCircuit(instruction_list=instruction_list)
