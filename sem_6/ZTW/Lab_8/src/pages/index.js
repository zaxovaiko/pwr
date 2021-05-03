import React, { useState } from 'react'
import { Link, graphql } from "gatsby"
import Layout from "../layouts"


const IndexPage = ({ data }) => {

  const [state, setState] = useState({
    filteredPosts: [],
    query: "",
  });

  const allPosts = data.allMarkdownRemark.edges;

  const handleInputChange = event => {
    const query = event.target.value;
    const filteredPosts = allPosts.filter(post => {
      const { title } = post.node.frontmatter;
      return (
        title.toLowerCase().includes(query.toLowerCase()) 
      );
    });
    setState({
      query,
      filteredPosts,
    });
  };

  const posts = state.query ? state.filteredPosts : allPosts;

  return (
    <Layout>
       <input
        type="text"
        aria-label="Search"
        placeholder="Search posts"
        value={state.query}
        onChange={handleInputChange}

        style={{marginBottom: '20px', width: '400px'}}
      />
      <div className="row g-3">
        {posts.map(({ node }, i) => (
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
