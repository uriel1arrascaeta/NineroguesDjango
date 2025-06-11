import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function PostList() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchPosts() {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/posts/');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setPosts(data);
            } catch (e) {
                console.error("Error fetching posts:", e);
                setError(e.message);
            } finally {
                setLoading(false);
            }
        }

        fetchPosts();
    }, []);

    if (loading) return <p>Loading posts...</p>;
    if (error) return <p>Error fetching posts: {error}</p>;

    return (
        <div>
            <h1>Blog Posts</h1>
            {posts.length > 0 ? (
                <ul>
                    {posts.map(post => (
                        <li key={post.id}>
                            <h2><Link to={`/blog/${post.slug}`}>{post.title}</Link></h2>
                            <p>{post.excerpt}</p>
                            <p>
                                <small>
                                    Published on: {new Date(post.published).toLocaleDateString()}
                                    {post.author ? ` by ${post.author}` : ''}
                                    {post.category ? ` in ${post.category.name}` : ''}
                                </small>
                            </p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No posts available.</p>
            )}
        </div>
    );
}

export default PostList;
