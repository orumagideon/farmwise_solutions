import React, { useEffect, useState } from "react";
import { getForumPosts } from "../api";
import "./Forum.css";

const Forum = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const data = await getForumPosts();
        setPosts(data);
      } catch (error) {
        console.error("Error fetching forum posts:", error);
      }
    };
    fetchPosts();
  }, []);

  return (
    <div className="forum-page">
      <h1>Farmers Forum</h1>
      <ul className="forum-list">
        {posts.map((post) => (
          <li key={post.id} className="forum-item">
            <h3>{post.title}</h3>
            <p>{post.content}</p>
            <p>Posted by: {post.username}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Forum;