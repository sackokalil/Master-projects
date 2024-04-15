import basic1  
import os



def read_file_or_input():
    while True:
        file_path = input("Enter file path (or type 'q' to quit) : ")

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
                        
                        print("\n** TOKENLIST **\n", tokens)
                        
                        print("\n** ARBRE SYNTAXIQUE ABSTRAIT **\n", ast.node)
                        
                        #basic1.PrintNode.print_node(ast.node)    # PrintNode class from basic1
                     
                        print("\n** INSTRUCTIONS INTERMÉDIAIRES GÉNÉRÉES **\n")
                        
                        for instruction in intermediate_code:
                            print(instruction)
                            
                        print("\n** RÉSULTAT FINAL **\n", result)
                        
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
                    print (f"\n** TOKENLIST **\n{tokens}")
                    
                    print (f"\n** ARBRE SYNTAXIQUE ABSTRAIT **\n{ast.node}")
                    
                    #basic1.PrintNode.print_node(ast.node)
                    
                    print (f"\n** INSTRUCTIONS INTERMÉDIAIRES GÉNÉRÉES **\n")
                    
                    for intermediate_instruction in intermediate_code:
                        print(intermediate_instruction)
                        
                    print (f"\n** RÉSULTAT FINAL **\n{result}")
                break  


read_file_or_input()
