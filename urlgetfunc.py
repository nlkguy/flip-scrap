import get_para from get_parameters

def url_get() :
    #"https://www.flipkart.com/search?q=[----search term----]"

    base_url='https://www.flipkart.com/search?q='

    term_q=input("\nEnter the Product name or Query : ")
    
    main_url=base_url+term_q

    return main_url
