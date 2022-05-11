# line2picture 
Wangdrak Dorji, Neophytos Christou, Truong Cai, TaShawn Arabian	

## Introduction

We are implementing the GAN described in the paper “Image-to-Image Translation with Conditional Adversarial Networks” by Prof.  Efros’ group at UC Berkeley. Their main objective in this paper is to investigate conditional GAN as a general strategy for solving image-to-image translation problems. They want their network to essentially not only learn the mapping from one image to another, but also learn the loss function that would train this mapping. After showing the theoretical framework, they proceed to show that they can successfully apply this technique to synthesized data such as “label maps, reconstructing objects from edge maps, and colorizing images.” 
We chose this paper because the program associated with it, pix2pix, is rather popular with artists who used it to generate interesting art. As a group we want to generate nice paintings, but given our collective lack of artistic skills, we thought that this project could help us achieve our dream. We train the model to learn to generate images of faces from pictures containing the outline of the face.	
This problem could be considered as both supervised and unsupervised learning depending on the approach. But essentially we are trying to generate a mapping to take images from source domain to target domain. Also specifically, the GAN approach is somewhat related to the Actor-Critic techniques in Reinforcement Learning (except there’s proof of convergence for AC but not GAN).

## Methodology

The dataset we used is called “Labeled faces in the wild” (http://vis-www.cs.umass.edu/lfw/) consisting of ~13K images of human faces. To generate outlines, we applied the Canny filter on the original dataset after upscaling everything to 256x256. We also tried running on a dataset containing pictures of shoes (https://vision.cs.utexas.edu/projects/finegrained/utzap50k/ut-zap50k-images.zip) to compare how our model performs on that compared to the face dataset.
Our model is a Generative Adversarial Network (GAN). Specifically, it is a Conditional GAN, similar to the one implemented in the original pix2pix paper. To train the model, we did a 3:1 partition of the dataset for training and testing. By playing around with the hyperparameters, we discovered that the optimal learning rate is 0.002 and the optimal batch size is 1. For the generator, we implemented the encoder-decoder architecture described in section 6.1.1 of the paper (Fig. 1), including skip connections. For the discriminator, we implemented the 70x70 PatchGAN described in the paper. For optimizing the loss, used mini batch SGD and applied the Adam solver. 

The generator architecture consists of:
encoder:
C64-C128-C256-C512-C512-C512-C512-C512
Decoder (U-net):
CD512-CD1024-CD1024-C1024-C512-C256-C128
The 70 × 70 discriminator architecture is: C64-C128-C256-C51
All convolution is done with stride of 2 followed by ReLU with slopes of 0.02

 
## Evaluation metric
There is no particular notion of accuracy or established objective way to evaluate the quality of generated images from generative models like ours. However, a popular metric for GAN outputs is called the “Inception Score” which is the measure of how realistic a GAN’s output is or an automated alternative which correlates well with human evaluation of realistic image quality. where the quality of synthesized images are rated based on a pre-trained Inception model’s ability to classify them.  We originally planned to use the “FCN-score” measure outlined in the pix2pix paper for our implementation as a measure of success for how realistic the model outputs are but due to recurrent bugs in transferring the code, we had to resort to using another measure of inception score known as the Frechet Inception Distance (FID) score. The FID score is also a metric that estimates the quality of generated images specifically for the performance of generative adversarial networks which is based on how well the top-performing image classification model Inception v3 classifies the generated and real image. A lower FID indicates better-quality images whereas a higher score indicates a lower-quality image. when fed our dataset of portrait outlines into the The original pix2pix had an FID  score of 32.69 when fed 1000 generated images along with their real image whereas our implementation had an FID  score of 24.08 indicating that our generated images of portraits were more realistic.
 

## Challenges

The most challenging part of our implementation was fine tuning the model to work in this specific domain. Pix2pix has been applied to similar datasets, such as generating pictures of bags from outlines, however our domain is a bit more complicated (portraits instead of bags, which have more details) and doesn’t contain as many images (the bags dataset contained 137K images, whereas ours contains only 1/10th of that).  Also as the bulk of our data were middle aged white males, the model has learnt to generate and apply those features to any outline input.  Hence, the performance in generating the  faces is not very good when generating outlines for individuals from other groups.

Another issue we faced was that at some point, our generator kept generating one-color, brown-ish pictures, which kept fooling the discriminator. To overcome this, we increased the dropout in the decoder part of the generator.

We notice that the quality of the input outline matters a lot, basically the model generates an output that really adheres to the outlines given to it. As an example, because the outline of the shoe, as shown above in that particular example, doesn’t show the outsoles. The model fails to draw the outsoles, despite many other training examples showing outline with outsoles. So it seems that the generator really here just fills in the blank rather than inferring what features supposedly should be there.

Finally, we had a hard time getting the model to converge. Regardless of how many training steps we had, the losses of both the generator and the discriminator kept fluctuating.

## Reflection

After looking back at line2picture as a whole, our group is very satisfied with the results we ended up with. Our biggest worry was that the complexity of the inputs we used would not produce images that were close to the original, thankfully the outputs that we produced were, in our eyes, successful. It is obvious that the images our project created were different from the original inputs, but there are clear resemblances and it aligns very well with what our initial goals and expectations were.  We expected our model to work similarly to one used within the original paper, this is quite apparent through how our approach changed over time. Throughout the project we tried experimenting with many different hyperparameters and tuning of our model, but we concluded that the optimal choices were the values that were closely related to ones used in the original paper. If we could have done anything differently if we could do the project over again, we would have initially gone with the values close to the original paper. This is because we spent significant time on experimenting and we believe that if we had more time we could have produced better results. That being said, with more time, we would have further experimented with the pre-processing of the images and the creation of the outlines to try to figure out if more detailed outlines would help produce better results or not. Additionally we would’ve liked to take time in attempting to reduce the artifacts that were in the output images we produced. Our biggest takeaways were essentially just how difficult it is to actually make a model that only somewhat “works”. The amount of time and effort that needs to be put in, is way more than any of us could have expected and we were still modeling after an idea that's already been made up, doing this from scratch would be exponentially more difficult. Another big takeaway was the idea that deep learning models are definitely the future. As we stated in our introduction, none of us are artists, but I would say the outputs we created could definitely be interpreted as art. Especially with digital art becoming so popular, we could definitely see models like this being used, and that's just one little part of what deep learning has to offer to our future. Finally our last takeaway was just how fun it was to come together with a group and complete a project that is somewhat significant. Seeing how the output produced gradually improved was both satisfying and rewarding, it was nice to see the knowledge we accumulated from the semester be used for a bigger project. 
