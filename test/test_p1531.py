"""Test for Beecrowd exercise 1531."""

from io import StringIO, BytesIO, TextIOWrapper
import os
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1531 import main as p1531
from python.p1531 import main_bytes as p1531_bytes


@pytest.mark.parametrize(
  "input_data, expected_output",
  [
    (
      (
        "1 100\n"
        "2 100\n"
        "3 100\n"
        "4 100\n"
        "5 100\n"
        "5 2\n"
        "6 100\n"
      ),
      "1\n1\n1\n2\n5\n1\n21\n",
    ),
    (
      (
        "1000000000 1000000\n"
        "999999937 999983\n"
        "123456789 98765\n"
        "111111111 2\n"
      ),
      "781250\n230327\n27537\n1\n",
    ),
  ],
)
def test_exercise_1531(
  monkeypatch: MonkeyPatch,
  capfd: CaptureFixture[str],
  input_data: str,
  expected_output: str,
):
  """Test for Beecrowd exercise 1531."""
  monkeypatch.setattr(sys, "stdin", StringIO(input_data))

  p1531()

  captured = capfd.readouterr()

  assert captured.out == expected_output


@pytest.mark.parametrize(
  "input_data, expected_output",
  [
    (
      (
        "1 100\n"
        "2 100\n"
        "3 100\n"
        "4 100\n"
        "5 100\n"
        "5 2\n"
        "6 100\n"
      ),
      "1\n1\n1\n2\n5\n1\n21\n",
    ),
    (
      (
        "1000000000 1000000\n"
        "999999937 999983\n"
        "123456789 98765\n"
        "111111111 2\n"
      ),
      "781250\n230327\n27537\n1\n",
    ),
  ],
)
def test_exercise_1531_bytes(
  input_data: str,
  expected_output: str,
):
  """Test for Beecrowd exercise 1531."""
  r_in, w_in = os.pipe()
  r_out, w_out = os.pipe()

  # Guardar stdin y stdout originales
  stdin_fd = os.dup(0)
  stdout_fd = os.dup(1)

  try:
    # Redirigir stdin y stdout
    os.dup2(r_in, 0)
    os.dup2(w_out, 1)

    # Escribir input en el pipe de entrada
    os.write(w_in, input_data.encode())
    os.close(w_in)
    os.close(r_in)

    # Ejecutar la función
    p1531_bytes()

    # Cerrar escritura para leer sin bloqueo
    os.close(w_out)

    # Leer la salida capturada
    output = os.read(r_out, 1 << 20).decode()

    # Verificar
    assert output == expected_output
  finally:
    # Restaurar stdin y stdout
    os.dup2(stdin_fd, 0)
    os.dup2(stdout_fd, 1)
    os.close(stdin_fd)
    os.close(stdout_fd)
    os.close(r_out)
