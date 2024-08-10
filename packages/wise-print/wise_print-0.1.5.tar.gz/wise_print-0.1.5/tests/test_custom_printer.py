from unittest.mock import patch
import pytest
import builtins
import inspect
from io import StringIO
from datetime import datetime
from wise_print.custom_printer import CustomPrinter

@pytest.fixture
def mock_datetime():
    with patch("datetime.datetime") as m:
        m.utcnow.return_value.isoformat.return_value = (
            "2024-08-09T18:15:00"
        )
        yield m

@pytest.fixture
def custom_printer():
    original_print = builtins.print
    printer = CustomPrinter()
    
    yield printer
    
    builtins.print = original_print

def test_print_with_time(custom_printer, mock_datetime):
    printer = custom_printer
    printer.include_time = True
    printer.include_file = False
    printer.include_line = False
    printer.activate()
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Test message")
            output = fake_out.getvalue().strip()
            time_log = datetime.now().isoformat(timespec='seconds')
            assert output.startswith(time_log), f"Expected the output to start with the timestamp. Got: {output}"
            assert "Test message" in output, "Original message should be included in the output"

def test_print_with_file_and_line(custom_printer, mock_datetime):
    printer = custom_printer
    printer.include_time = False
    printer.include_file = True
    printer.include_line = True
    printer.activate()
    print("Test message")
    
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Test message")
            output = fake_out.getvalue().strip()
            assert __file__ in output, f"Expected the output to include the filename. Got: {output}"
            assert "Test message" in output, "Original message should be included in the output"
            line_number = str(inspect.currentframe().f_lineno - 4)
            assert line_number in output, f"Expected the output to include the line number. Got: {output}"

def test_print_with_custom_separator(custom_printer, mock_datetime):
    printer = custom_printer
    printer.include_time = True
    printer.include_file = True
    printer.include_line = True
    printer.separator = " | "
    printer.activate()
    print("Test message")
    
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Test message")
            output = fake_out.getvalue().strip()
            assert " | " in output, f"Expected the output to use the custom separator. Got: {output}"
            assert "Test message" in output, "Original message should be included in the output"

def test_print_without_any_extra_info(custom_printer, mock_datetime):
    printer = custom_printer
    printer.include_time = False
    printer.include_file = False
    printer.include_line = False
    printer.activate()
    print("Test message")
    
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Test message")
            output = fake_out.getvalue().strip()
            assert output == "Test message", f"Expected output to be just the original message. Got: {output}"

def test_activate_deactivate(custom_printer, mock_datetime):
    printer = custom_printer
    
    printer.activate()
    print("Test message")
    
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Test message")
            output = fake_out.getvalue().strip()
            assert "Test message" in output, "Custom print should be active and capture the output"
    
    printer.deactivate()
    with patch('sys.stdout', new = StringIO()) as fake_out: 
            print("Another message")
            output = fake_out.getvalue().strip()
            assert output == "Another message", "Custom print should be deactivated and original print should be restored"
