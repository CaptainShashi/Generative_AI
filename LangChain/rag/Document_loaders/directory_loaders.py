# loads multiple document from a directory (folder) fo file 
#    ** = recursive search through folder 
#    '**/*.text' --->text files 
#    '*.csv'     ---> all csv files 
#    '**/*'      ---> all files 


from langchain.document_loaders import DirectoryLoader, PyPDFLoader

loaders=DirectoryLoader(
    path="path to that folder",
    glob='*.pdf' , # load all pdf 
    loader_cls=PyPDFLoader
)

docs=loaders.load()

print(docs)