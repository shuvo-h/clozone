from flask import Blueprint, jsonify, request
from src.app_server.utils.resSender import send_res
from . import test_controller

test_bp = Blueprint('test_bp',__name__)

new_blog_content = """

 <main>
        <section>
            <p>In the competitive e-commerce landscape, visibility is crucial for attracting clients. Google My Business (GMB) offers a powerful way to enhance your online presence and stand out from the competition.</p>
        </section>

        <section>
            <h2>Key Strategies for Success</h2>
            <p><strong>1. Create a Strong Profile:</strong> Ensure your GMB listing is complete with accurate contact information. A visible phone number enhances credibility and engagement.</p>
            <p><strong>2. Showcase Your Work:</strong> Use GMB's photo features to display your design portfolio, helping potential clients visualize your expertise.</p>
            <p><strong>3. Engage with Reviews:</strong> Respond to client feedback to build trust and demonstrate your commitment to excellent service.</p>
            <p><strong>4. Leverage Local SEO:</strong> Include relevant keywords in your GMB description to improve search visibility and attract more e-commerce clients.</p>
        </section>

        <section>
            <p>By optimizing your GMB profile, you not only enhance your visibility but also build stronger client relationships and drive business growth.</p>
        </section>
    </main>

"""

@test_bp.post("/contextual_internal_link")
def createContextualLink():
    # new_blog_content = "<p>This is your new blog content where some key phrases will be replaced by internal links.</p>"

    result = test_controller.createContexualInternalLink(new_blog_content=new_blog_content)

    return send_res(
        status=201,
        data=result,
        message='test api responding'
    )






