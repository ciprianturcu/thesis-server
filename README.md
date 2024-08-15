
# Thesis Server - FastAPI Inference Server

The server is a FastAPI server designed to load a [HuggingFace model](https://huggingface.co/SEBIS/code_trans_t5_large_code_comment_generation_java_multitask_finetune) specialized in generating comments for code snippets. The server provides a RESTful endpoint where users can submit code via a POST request. The server processes this input, utilizes the loaded model to generate corresponding comments, and returns the results in a structured response.




## Installation

#### Prerequisites:
Python (3.10) with pip for package installation

#### Steps:
1. Create a virtual environment running the specified python version.
2. Clone the repository
3. Navigate to the project directory

4. Install with pip the required packages

```bash
  pip install -r requirements.txt
```
5. Run the server

```bash2 
  uvicorn main:app --host 0.0.0.0 --port 8080
```


## API Reference

#### Generate comment for code

```http
  POST /getComment
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `string` | **Required**. Code text to generate a comment for |


Example Response

```json
{
  "summary_text": "This function adds two numbers and returns the result."
}
```
## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) [2024] [Turcu Ciprian-Stelian]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
