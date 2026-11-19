def main():

    # VARIABLES
    name = "MIT"
    age = 30
    salary = 85000.50

    age = 40

    print(age)

    # NUMERIC & ARITHMETICS
    x = 10
    y = 10.5

    print(type(x))
    print(type(y))

    # 运算符号 + - * /
    print(10/2) # /回返回float
    print(10 // 3) # 返回int，这叫floor division
    print(10 % 3) # %返回余数，这叫modulus
    print(2 ** 3) # **返回幂，这叫exponentiation

    #STRINGS
    name = "MIT"
    message = 'Hello, World!'

    #String Concatenation
    first_name = "Ibis"
    last_name = "Liu"
    full_name = first_name + " " + last_name
    message = f"Hello, {first_name} {last_name}" #f-string

    print("Hello " * 3) #output: Hello Hello Hello

    

if __name__ == "__main__":
    main()