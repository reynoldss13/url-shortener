import { Component } from '@angular/core';
import { APIService } from 'src/API/api.service';
import { FormBuilder } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Url Shortener';

  constructor(private APIService: APIService, private formBuilder: FormBuilder){}

  urlGenerationForm: any;
  urlOutputForm:any;
  generatedUrl:any;

  ngOnInit(){
    this.urlGenerationForm = this.formBuilder.group({urlInput:[]});
    this.urlOutputForm = this.formBuilder.group({});
  }

  submit(url:any){
    this.APIService.generateUrl(url).subscribe((response:any) => {
      this.generatedUrl = response['data'];
      document.getElementById('output')?.classList.remove('hidden');
    }, err =>{
      alert("Invalid URL!");
    });
  }

  copyLink(urlText:any){
  
  }
}
