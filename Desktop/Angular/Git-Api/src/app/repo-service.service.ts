import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import{ environment } from '../environments/environment';
import { Observable, from } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RepoServiceService {
  _URL = 'https://api.github.com/users/';
  token = '?access_token=8538e65840c701357470f29c5e08a2f443151a65';

  constructor(public  http: HttpClient) {

   }
   getRepo(searchTerm: string): Observable<any> {
    return this.http.get(this._URL + searchTerm + '/repos' + this.token);
  }
}



