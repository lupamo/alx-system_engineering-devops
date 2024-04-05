# HTTPS SSL

Hyper Text Transfer Protocol Secre (HTTPS) is the secure version of HTTP, the protocol over which data is sent between your browser and the website that you are connected to. HTTPS is often used to protect highly confidential online transactions like online banking and online shopping order forms.

## How Does HTTPS Work?

HTTPs pages typically use one of the two secure protocols to encrypt communications - SSL (Secure Socket Layer) or TLS (Transport Layer Security).
Both the TLS and SSL protocols use what is known as an "asymmetric" Public Key Infastructure (PKI) system.
An Asymetric system uses two 'keys' to encrypt communications  a 'Public Key' and a 'Private Key'.
As the names suggest, the 'private' key should be kept strictly protected and should only be accessible the owner of the private key. In the case of a website, the private key remains securely ensconced on the web server.

## What is a HTTPS certificate?

When you request a HTTPS connection to a webpage, the website will initially send its SSL certificate to your browser.
This certificate contains the public key needed to begiin the secure session.
Based on the initial exchange, your browser and the website then initiate the 'SSL handshake'. The SSL handshake involves the generation of shared secrets to establish a uniquely secure connection between yourself and the website.

## Why is an SSL Certifiate Required?

All commuications sent over regular HTTP connection are in 'plain text' and can be read by any hacker that manages to break into the connection between your browser and the website.
With a HTTPS connection, all communications are securely encrypted. This means that even if somebody managed to break into the connection, they would not be able decrypt any of the data which passes between you and the website.

## SSL Provides Authentication

In addition to encryption, a proper SSL certificate provides authentication. This means that you are sending information to the right server and not to an imposter trying to steal your information. 

## TLS temination Proxy

A TLS termination proxy (or SSL termination proxy,[1] or SSL offloading[2]) is a proxy server that acts as an intermediary point between client and server applications, and is used to terminate and/or establish TLS (or DTLS) tunnels by decrypting and/or encrypting communications.
