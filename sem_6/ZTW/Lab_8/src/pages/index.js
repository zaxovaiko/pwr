import * as React from "react"
import { Link, graphql } from "gatsby"
import Layout from "../layouts"

const IndexPage = ({ data }) => {
  return (
    <Layout>
      <div className="row g-3">
        {data.allMarkdownRemark.edges.map(({ node }, i) => (
          <div key={i} className="col-6">
            <div className="card">
              <div className="card-body">
                <Link
                  to={node.frontmatter.slug}
                  style={{ textDecoration: "none" }}
                >
                  <h3>{node.frontmatter.title}</h3>
                </Link>
                <p>Author: {node.frontmatter.author} <span className="float-end">{node.timeToRead} mins to read, {node.frontmatter.date}</span></p>
                <p>{node.excerpt}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </Layout>
  )
}

export const query = graphql`
  query HomePageQuery {
    allMarkdownRemark(sort: { fields: [frontmatter___date], order: DESC }) {
      totalCount
      edges {
        node {
          frontmatter {
            title
            date
            slug
            author
          }
          excerpt
          timeToRead
        }
      }
    }
  }
`

export default IndexPage
