
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include <unistd.h>
#include <string>
#include <iostream>
using namespace std;
//#define CURL_DEBUG 1
#define CURL_WAIT_TIMEOUT_MSECS 60000 //60s
#define CURL_MULIT_MAX_NUM 5

static size_t recive_data_fun( void *ptr, size_t size, size_t nmemb, void *stream){
        cout << "1111111111111111111111111111111111111111111111111111111111 " << endl;
    char head[12048] = {0};
    memcpy(head,ptr,size*nmemb+1);
    printf(" %s \n",head);
    return size*nmemb;
}

static size_t read_head_fun( void *ptr, size_t size, size_t nmemb, void *stream){
        cout << "222222222222222222222222222222222222222222222222222222222 " << endl;
    char head[2048] = {0};
    memcpy(head,ptr,size*nmemb+1);
    printf(" %s \n",head);
    return size*nmemb;
}

int main(int argc, char **argv)
{
    std::string url = "https://getman.cn/";
    CURL* curl_handle = curl_easy_init();

    if(curl_handle){
        cout << "fds " << endl;
        curl_easy_setopt(curl_handle, CURLOPT_URL, url.c_str());//set down load url
        //curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, save_file);//set download file
        curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, recive_data_fun);//set call back fun
        curl_easy_setopt(curl_handle, CURLOPT_HEADERFUNCTION, read_head_fun);//set call back fun

    //start down load
        CURLcode res = curl_easy_perform(curl_handle);
        printf("4444444444444444444444444444444444444444 %d\n",res);
    }

    if(curl_handle){
        cout << "3333333333333333333333333333333333333333333333333333 " << endl;
        curl_easy_cleanup(curl_handle);
    }


    return 0;
}