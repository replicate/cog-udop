## Cog Wrapper for UDOP

Cog wrapper for UDOP, a unified model by Microsoft for document classification, layout parsing and visual question answering.

See the [paper](https://arxiv.org/pdf/2212.02623.pdf), [model page](https://huggingface.co/microsoft/udop-large) and Replicate [demo](https://github.com/replicate/cog-udop) for more details.

## API Usage

You need to have Cog and Docker installed to run this model locally. To build the docker image with cog and run a prediction:

```cog predict -i image=@sample.jpg -i prompt="Question answering. How many items are sold?"```

To start a server and send requests to your locally or remotely deployed API:

```cog run -p 5000 python -m cog.server.http```

To use UDOP, you need to provide an image file and a text prompt describing the task you want to perform on the document. The API input arguments are as follows:

- **image**: Path to the input image file of the document.
- **prompt**: Text prompt for describing the task. 

## Usage Tips

Text prompt should contain both task definition and (if necessary) the task itself and they should be seperated by a point. For example,

- In the case of the question answering task, prompt  should be "Question answering. In which year is the report made?"
- However, for the document classification task, the prompt should be "Document classification."

## References

```
@misc{tang2023unifying,
      title={Unifying Vision, Text, and Layout for Universal Document Processing}, 
      author={Zineng Tang and Ziyi Yang and Guoxin Wang and Yuwei Fang and Yang Liu and Chenguang Zhu and Michael Zeng and Cha Zhang and Mohit Bansal},
      year={2023},
      eprint={2212.02623},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
