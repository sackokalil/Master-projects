import basic1  
import os



def read_file_or_input():
    while True:
        file_path = input("Enter file path or press enter to type text (or type 'q' to quit) : ")

        if file_path.lower() == 'q':
            break  # Quit the exection

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    tokens, ast, intermediate_code, result, error = basic1.run(file_path, text) # run function from basic1

                    if error:
                        print("An Error occured during text analysis: :")
                        print(error.as_string())
                    else:
                        
                        print("\n** TOKEN LIST **\n", tokens)
                        
                        print("\n** ABSTRACT SYNTAX TREE **\n", ast.node)
                        
                        #basic1.PrintNode.print_node(ast.node)    # PrintNode class from basic1
                     
                        print("\n** GENERATED INTERMEDIATE INSTRUCTIONS **\n")
                        
                        for instruction in intermediate_code:
                            print(instruction)
                            
                        print("\n** FINAL RESULT **\n", result)
                        
            except Exception as e:
                print("An error occured :", str(e))
        else:
            print("\nThe specified file doesn't exist. Please type the text :\n")
            while True:
                text = input('basic > ')
                tokens, ast, intermediate_code, result, error  = basic1.run('<stdin>', text)

                if error:
                    print(error.as_string())
                    
                else: 
                    print (f"\n** TOKEN LIST **\n{tokens}")
                    
                    print (f"\n** ABSTRACT SYNTAX TREE **\n{ast.node}")
                    
                    #basic1.PrintNode.print_node(ast.node)
                    
                    print (f"\n** GENERATED INTERMEDIATE INSTRUCTIONS **\n")
                    
                    for intermediate_instruction in intermediate_code:
                        print(intermediate_instruction)
                        
                    print (f"\n** FINAL RESULT **\n{result}")
                break  


read_file_or_input()
