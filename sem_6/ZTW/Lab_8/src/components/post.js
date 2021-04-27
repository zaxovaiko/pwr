import { graphql } from "gatsby"
import React from "react"
import { StaticImage } from "gatsby-plugin-image"
import { Disqus } from "gatsby-plugin-disqus"

import Layout from "../layouts/index"

export default function Post({ data }) {
  const post = data.markdownRemark
  return (
    <Layout>
      <div className="col-12">
        <StaticImage src="../images/post.jpg" alt="image" />
        <h1>{post.frontmatter.title}</h1>
        <h4 className="text-muted">
          {post.frontmatter.author}{" "}
          <span className="small float-end fs-5">{post.frontmatter.date}</span>
        </h4>
        <div className="mt-5" dangerouslySetInnerHTML={{ __html: post.html }} />
        <Disqus
          config={{
            url: `http://localhost:8000/${post.frontmatter.title}`,
            identifier: post.frontmatter.title,
            title: post.frontmatter.title,
          }}
        />
      </div>
    </Layout>
  )
}

export const query = graphql`
  query PostQuery($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        author
        date
      }
    }
  }
`
