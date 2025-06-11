import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';

function PostDetail() {
    const [post, setPost] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const { slug } = useParams();

    useEffect(() => {
        if (!slug) return;

        async function fetchPostDetail() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/posts/${slug}/`);
                if (!response.ok) {
                    if (response.status === 404) {
                        throw new Error('Post not found');
                    }
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setPost(data);
            } catch (e) {
                console.error("Error fetching post detail:", e);
                setError(e.message);
            } finally {
                setLoading(false);
            }
        }

        fetchPostDetail();
    }, [slug]); // Volver a ejecutar si el slug cambia

    if (loading) return <p>Loading post details...</p>;
    if (error) return <p>Error: {error}</p>;
    if (!post) return <p>Post not found.</p>;

    return (
        <div>
            <Link to="/blog">Back to Blog</Link>
            <h1>{post.title}</h1>
            {post.author && <p><small>By: {post.author}</small></p>}
            {post.category && <p><small>Category: {post.category.name}</small></p>}
            <p><small>Published: {new Date(post.published).toLocaleDateString()}</small></p>
            <hr />
            <div dangerouslySetInnerHTML={{ __html: post.content }} /> {/* Si el contenido es HTML */}
            {/* O simplemente: <p>{post.content}</p> si es texto plano */}
        </div>
    );
}

export default PostDetail;
