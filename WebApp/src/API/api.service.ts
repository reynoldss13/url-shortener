// API Service component is used to call the Flask API
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';


@Injectable()
export class APIService {
    constructor(private http: HttpClient, private router: Router) {}

    generateUrl(url:any){
        let fd = new FormData();
        fd.append('url', url);
        return this.http.post('http://127.0.0.1:5000/generate',fd);
    }

    getUrl(id:any){
        return this.http.get('http://127.0.0.1:5000/'+id);
    }

}