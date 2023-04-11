import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'dimensionlessaifrontend';

  constructor(private http: HttpClient) {}

  newFile(fileInput:any) {

    let fi = fileInput;

    if (fi.files && fi.files[0]) {
      let fileToUpload = fi.files[0];

      let formData: FormData = new FormData();
      formData.append("file", fileToUpload);
      this.http.post('http://127.0.0.1:8000/upload', formData).subscribe(
      data => console.log(data),
      error => console.log(error)
    );
  }
  }

  getFile(start_date:any,end_date:any) {
    console.log(start_date)
    console.log(end_date)
    let postData = {
      start_date,
      end_date
    }
    this.http.post('http://127.0.0.1:8000/fetchfile', postData).subscribe(
      data => console.log(data),
      error => console.log(error)
    )
  }
}
