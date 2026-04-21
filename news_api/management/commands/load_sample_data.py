from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from news_api.models import NewsArticle


class Command(BaseCommand):
    help = 'Load sample news data into the database'

    def handle(self, *args, **options):
        sample_data = [
            {
                'id': '1',
                'title': 'Breaking: Major Tech Company Announces Revolutionary AI Breakthrough',
                'description': 'A leading technology company has unveiled a groundbreaking artificial intelligence system that promises to transform how we interact with technology in ways previously thought impossible. This revolutionary AI breakthrough represents years of intensive research and development, combining cutting-edge machine learning algorithms with advanced neural network architectures. The system demonstrates unprecedented capabilities in natural language processing, computer vision, and complex problem-solving tasks. Industry experts are calling this development a watershed moment that could fundamentally change the landscape of artificial intelligence applications across multiple sectors including healthcare, finance, education, and entertainment. The technology features enhanced reasoning capabilities, improved contextual understanding, and the ability to generate highly accurate and relevant responses to complex queries. Early testing phases have shown remarkable improvements in efficiency and accuracy compared to existing AI systems. The company plans to gradually roll out this technology through strategic partnerships and enterprise solutions, with consumer applications expected to follow in the coming months. This breakthrough has already garnered significant attention from investors, researchers, and technology leaders worldwide, with many predicting it will accelerate the adoption of AI solutions across various industries and potentially create new market opportunities worth billions of dollars.',
                'urlToImage': 'https://share.google/images/47AC9Zl1LQnPyGgLF',
                'publishedAt': '2024-01-15T10:00:00Z',
                'source': {'name': 'Tech Today'},
                'category': 'technology',
                'url': 'https://example.com/tech-news-1'
            },
            {
                'id': '2',
                'title': 'Global Climate Summit Reaches Historic Agreement',
                'description': 'World leaders have reached an unprecedented consensus on climate action, setting ambitious targets for the next decade that could fundamentally reshape global environmental policies and economic strategies. This historic agreement, negotiated over weeks of intensive discussions involving representatives from 195 countries, establishes comprehensive frameworks for reducing greenhouse gas emissions, transitioning to renewable energy sources, and implementing sustainable development practices across all major sectors. The summit addressed critical issues including carbon pricing mechanisms, international cooperation on clean technology development, and financial support for developing nations to achieve their climate goals. Key provisions include mandatory emission reduction targets of 50% by 2030, increased investment in renewable energy infrastructure, and the establishment of a global carbon trading system. The agreement also outlines specific measures for protecting biodiversity, combating deforestation, and promoting sustainable agriculture practices. Environmental scientists and policy experts have praised the agreement as a significant step forward in addressing the climate crisis, while acknowledging the substantial challenges that lie ahead in implementation. The economic implications are far-reaching, with projections suggesting the need for trillions of dollars in investment to achieve the stated goals. Industry leaders across various sectors are already beginning to adapt their strategies to align with the new targets, recognizing both the challenges and opportunities presented by this transformative agreement.',
                'urlToImage': 'https://share.google/images/47AC9Zl1LQnPyGgLF',
                'publishedAt': '2024-01-15T08:30:00Z',
                'source': {'name': 'Global News'},
                'category': 'general',
                'url': 'https://example.com/climate-news-1'
            },
            {
                'id': '3',
                'title': 'Stock Markets Reach New Heights Amid Economic Recovery',
                'description': 'Major stock indices continue their remarkable upward trajectory as economic indicators show increasingly strong recovery signs, driven by a combination of robust corporate earnings, favorable monetary policies, and renewed investor confidence in long-term growth prospects. The sustained market rally has been particularly notable in technology, healthcare, and renewable energy sectors, which have demonstrated exceptional resilience and growth potential throughout the recovery period. Financial analysts attribute this positive momentum to several key factors including improved employment rates, increased consumer spending, successful vaccine distribution programs, and strategic government stimulus measures that have effectively supported both businesses and individuals during challenging times. Corporate earnings reports have consistently exceeded expectations, with many companies reporting record profits and optimistic forward guidance for upcoming quarters. The technology sector has been a particular standout, benefiting from accelerated digital transformation trends and increased demand for innovative solutions across various industries. Healthcare companies have also performed exceptionally well, driven by breakthrough medical treatments and increased investment in research and development. Meanwhile, the renewable energy sector has attracted significant capital as investors recognize the long-term potential of sustainable technologies. Market volatility has remained relatively low, suggesting strong underlying stability and confidence in economic fundamentals. However, some economists caution that valuations may be approaching levels that warrant careful consideration, and investors should remain mindful of potential risks including inflation concerns and geopolitical uncertainties.',
                'urlToImage': 'https://share.google/images/47AC9Zl1LQnPyGgLF',
                'publishedAt': '2024-01-15T07:15:00Z',
                'source': {'name': 'Financial Times'},
                'category': 'business',
                'url': 'https://example.com/business-news-1'
            },
            {
                'id': '4',
                'title': 'Championship Final Set for This Weekend',
                'description': 'Two powerhouse teams prepare for the ultimate showdown in what promises to be the game of the century, as months of intense competition culminate in a championship final that has captured the attention of sports fans worldwide. Both teams have demonstrated exceptional skill, determination, and strategic prowess throughout the season, overcoming numerous challenges and defeating formidable opponents to earn their place in this prestigious final. The road to the championship has been marked by thrilling victories, dramatic comebacks, and outstanding individual performances that have showcased the highest levels of athletic excellence. Team preparation has been intense and meticulous, with coaches analyzing every aspect of their opponents strategies, player statistics, and historical performance data to develop comprehensive game plans. Players have undergone rigorous training regimens, focusing on physical conditioning, tactical execution, and mental preparation to ensure peak performance when it matters most. The stakes could not be higher, as victory would not only bring the coveted championship title but also significant financial rewards, enhanced reputation, and lasting legacy for the winning organization. Media coverage has been extensive, with expert analysts providing detailed breakdowns of team strengths, key matchups, and potential game-changing factors. Ticket demand has reached unprecedented levels, with fans traveling from around the world to witness this historic sporting event. The economic impact on the host city is expected to be substantial, with hotels, restaurants, and local businesses preparing for the influx of visitors. Both teams have expressed confidence in their abilities while maintaining respect for their opponents, setting the stage for what many predict will be an unforgettable contest.',
                'urlToImage': 'https://share.google/images/47AC9Zl1LQnPyGgLF',
                'publishedAt': '2024-01-15T06:00:00Z',
                'source': {'name': 'Sports Central'},
                'category': 'sports',
                'url': 'https://example.com/sports-news-1'
            },
            {
                'id': '5',
                'title': 'New Medical Breakthrough Offers Hope for Rare Disease',
                'description': 'Researchers have developed a promising new treatment that could help millions of patients worldwide suffering from a rare genetic disorder that has previously had limited therapeutic options. This groundbreaking medical breakthrough represents the culmination of over a decade of intensive research involving international collaboration between leading medical institutions, pharmaceutical companies, and patient advocacy groups. The innovative treatment approach utilizes advanced gene therapy techniques combined with novel drug delivery systems to target the underlying molecular mechanisms responsible for the disease. Clinical trial results have shown remarkable efficacy in treating symptoms and potentially slowing disease progression, offering new hope for patients and families who have long awaited effective treatment options. The research team employed cutting-edge biotechnology tools including CRISPR gene editing, personalized medicine approaches, and artificial intelligence-assisted drug discovery to develop this revolutionary therapy. Patient safety and treatment effectiveness have been rigorously evaluated through multiple phases of clinical testing, with independent monitoring boards ensuring the highest standards of medical research ethics and patient protection. The treatment has received fast-track designation from regulatory authorities, recognizing its potential to address a significant unmet medical need. Healthcare professionals specializing in rare diseases have expressed optimism about the potential impact of this breakthrough, while emphasizing the importance of continued research and development to refine treatment protocols and expand access to patients. The pharmaceutical company behind this development has committed to making the treatment accessible through various patient assistance programs and is working with insurance providers to ensure coverage. This medical advancement also opens new avenues for treating related genetic disorders and demonstrates the potential of modern biotechnology to address previously intractable medical conditions.',
                'urlToImage': 'https://share.google/images/47AC9Zl1LQnPyGgLF',
                'publishedAt': '2024-01-15T05:30:00Z',
                'source': {'name': 'Medical Journal'},
                'category': 'health',
                'url': 'https://example.com/health-news-1'
            },
        ]

        self.stdout.write('Loading sample news data...')
        
        for item in sample_data:
            # Parse the published date
            published_at = datetime.strptime(item['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            published_at = timezone.make_aware(published_at)
            
            # Create or update the news article (simplified - no separate source table)
            article, created = NewsArticle.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'url_to_image': item['urlToImage'],
                    'published_at': published_at,
                    'source_name': item['source']['name'],  # Direct field instead of ForeignKey
                    'category': item['category'],
                    'url': item['url'],
                }
            )
            
            if created:
                self.stdout.write(f'Created article: {article.title}')
            else:
                self.stdout.write(f'Updated article: {article.title}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(sample_data)} news articles')
        )