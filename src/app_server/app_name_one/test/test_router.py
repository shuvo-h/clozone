from flask import Blueprint, jsonify, request
from src.app_server.utils.resSender import send_res
# from . import test_controller,topic_ln
# from . import LSI_keyword, LSI3Way
# from . import LSI_advance
# from .sh_pack import linkFinder_BERT
# from .sh_pack import linkFinder_distilBERT
from .sh_pack import context_linker



test_bp = Blueprint('test_bp',__name__)

new_blog_content = """

 <main>
    <article>
        <header>
            <h1>5 LinkedIn Strategies for Designers to Captivate Event Planners: Stand Out in the Crowd</h1>
            <p>In the dynamic realm of event planning, where creativity and innovation are paramount, designers have the power to turn visions into unforgettable realities. LinkedIn, as the premier professional network, offers an excellent platform for designers to connect with event planners and showcase their expertise.</p>
        </header>

        <section>
            <h2>1. Create a Captivating Profile That Reflects Your Unique Design Perspective</h2>
            <p>Your LinkedIn profile is often the first interaction potential clients have with you. Ensure it captures the essence of your design philosophy and the distinct value you bring to event planning. Start with a high-quality profile picture and a banner image that showcases your design style.</p>
            <p>Use the summary section to craft a compelling narrative about your career journey, inspirations, and the reasons why event planners should consider you for their upcoming events. Clearly articulate your areas of specialization, whether it's luxurious floral arrangements, cutting-edge lighting designs, or bespoke event setups.</p>
        </section>

        <section>
            <h2>2. Highlight Your Work with Engaging Visuals</h2>
            <p>Event planners are highly visual and are constantly searching for fresh, innovative ideas to enhance their events. Take advantage of LinkedIn’s rich media features to create a visually appealing portfolio. Upload high-quality images, videos, and slideshows of your past projects, showcasing the full spectrum of your work.</p>
            <p>Feature events where your design played a pivotal role, from intimate gatherings to large-scale corporate functions, to demonstrate your versatility and expertise.</p>
        </section>

        <section>
            <h2>3. Share Insightful Articles and Posts on Design Trends</h2>
            <p>Position yourself as a thought leader by publishing articles and posts that delve into the latest trends and innovations in event design. Topics could include sustainable design practices, advancements in event technology, or unique thematic concepts.</p>
            <p>Consistent, informative content will keep you at the forefront of event planners' minds, showcasing your industry knowledge and design prowess.</p>
        </section>

        <section>
            <h2>4. Build Your Reputation with Recommendations and Endorsements</h2>
            <p>In event planning, reputation is crucial. Request recommendations from past clients, colleagues, and industry partners to enhance your credibility. These testimonials serve as social proof of your skills and reliability, giving event planners confidence in your ability to deliver exceptional results.</p>
            <p>A strong recommendation can be a deciding factor for event planners when choosing a design partner.</p>
        </section>

        <section>
            <h2>5. Actively Engage with the Event Planning Community</h2>
            <p>LinkedIn is not just for self-promotion; it’s a vibrant community. Follow event planning groups, companies, and influencers. Participate in discussions, comment on posts, and share relevant content to increase your visibility.</p>
            <p>Active engagement not only enhances your profile’s visibility but also fosters connections with event planners, opens up collaboration opportunities, and provides insights into industry needs and trends.</p>
        </section>

        <footer>
            <h3>Additional Tips for Maximizing Your LinkedIn Presence</h3>
            <p><strong>How often should you update your LinkedIn profile?</strong> Regular updates are key. Aim to refresh your profile every 3-6 months or when you achieve significant milestones or complete notable projects.</p>
            <p><strong>What content resonates with event planners?</strong> Share content that highlights your design expertise and addresses relevant event planning trends. Include case studies, design process insights, and tips for creating standout events.</p>
            <p><strong>How to network with event planners if you’re new to the industry?</strong> Start by engaging with event planning groups and influencers. Comment on relevant posts, share your thoughts, and send personalized connection requests to introduce yourself and express your interest in their work.</p>
        </footer>
    </article>
</main>


"""

@test_bp.post("/contextual_internal_link")
def createContextualLink():
    # new_blog_content = "<p>This is your new blog content where some key phrases will be replaced by internal links.</p>"

    # result = test_controller.createContexualInternalLink(new_blog_content=new_blog_content)
    # result = topic_ln.add_relevant_links(new_blog_html=new_blog_content,domain="https://biddrup.com")
    result = {"ok":"Okay Test"}
    return send_res(
        status=201,
        data=result,
        message='test api responding'
    )


@test_bp.post('/collect_contextual_link')
def collectContextualLink():
    body = request.get_json()
    keywords=[]
    blogs=[]
    contextual_links=[]
    result = context_linker.collect_context_links(body['new_blog'])

    return send_res(
        status=201,
        data=result,
        message='Collected contextual links'
    )



