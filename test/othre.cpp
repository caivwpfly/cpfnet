    if(argc < 3){
        printf("arg1 is url; arg2 is out file\n");
        return -1;
    }    
    char* url = strdup( argv[1]);
    char* filename= strdup(argv[2]);
    CURL* curl_handle;
    CURLcode res;
    
    //int
    FILE* save_file = fopen(filename,"w");
    if(save_file == NULL){
        printf("open save file fail!\n");
        return -1;
    }


    return fwrite(ptr,size,nmemb,(FILE*)stream);
    
    //release
    if(save_file){
        fclose(save_file);
        save_file = NULL;
    }

        if(url){
        free(url);
    }