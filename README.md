# Gandi

> Stateful Reverse Proxy for decentralized IT jobs

Gandi shifts the closed-platform job search paradigm to a distributed, transparent and job-seeker driven model, developing
capabilities to create unique job search engines that **share the same source of content** but provide **different
features** to retrieve and process it.

To put it simply, Gandi can be described as a company's job listings repository, which follows the following main principles:

- **Decentralized** – each company is responsible for its own job listings, that have been published on the company's
  website and pulled by Gandi;
- **Instant** – a single link to a company's job listing ensures seamless sync with Gandi repository, negating the need
  for manual content duplication;
- **Opensource** – all job listings are stored publicly and can be used by anyone for any purpose;
- **Consistent** – all job listings are synced with the company's website on a daily basis.

## Why?

Traditional job search tools tend to position themselves as intermediaries, but their approach often fragments the job
market. Different job platforms publish unique sets of job listings, resulting in scattered and sometimes outdated
information. This fragmented reality can mislead job-seekers and burden companies that struggle to keep listings up to
date across multiple platforms.

Job search platforms operate more like a _black box_ than a practical tool. Companies face competition, huge costs for
posting and advertising, and restrictions on how much information they can communicate about their vacancy.

Similarly, job-seekers struggle with _rigid search_ and filter options. Each platform restricts users to its pre-defined
categories and keywords, leaving little room for a customised job search experience. In essence, these issues make job
searching a daunting task rather than a smooth process.

![img_3.png](img_3.png)

The job search industry is also prohibitively difficult to enter from a startup solutions perspective because **it's
rooted in the content problem**. We're sure there are a myriad of alternative approaches to filtering, sorting,
personalised search and alerts, but they're all prohibitively difficult to implement for one simple reason: **the lack
of an easy way to access corporate careers**.

### Does it have to be this way?

The unambiguous hiring goals of the company – to find the best-fit employee, and the job-seeker – to find the best-fit
job, pushed us to the alternative solution space:

1. Job postings should be **as public as possible** – so that as many job-seekers as possible can find them;
2. Job platform business model **shouldn't cut off needy companies that cannot afford it**;
3. The more **personalised job search** and filtering tools that exist, the more candidates will be able to find the
   right vacancies;
4. Innovative job search systems **should answer the "How"** and **take the "What" for granted** to cover as many
   job-seeker preferences as possible.

That's exactly what Gandi is trying to achieve.
## Approach

To make sure we're on the same page, let's see how it should work in practice:

![img_5.png](img_5.png)

Gandi is deeply anchored around three main layers: pull-based careers retrieval engine, public careers storage, and custom data consumer implementations – specific search platforms.

### Retrieval engine
Gandi retrieves company job listings directly from the source. We ensure that the repository's data is directly fetched from the companies’ websites, reducing the chance for outdated, misleading or fragmented job offers. This approach also allows us to avoid the need for manual content duplication, as the __company's career page is the only source of truth__.

### Public Storage
All gathered job listings are stored publicly and __can be accessed by everyone, at all times__, right in this repository. By ensuring company job information is as public as possible, we feel this levels the playing field for all job-seekers, and enables maximum reach.


### Data Consumers
That approach won't work without consumers – systems that are able to pull the data from Gandi, implement a custom search engine based on that and fit the target audience – job-seeker needs.

It's crucial to understand that __Gandi is not a search engine itself__, though it's useless in a vacuum. We seek to provide a data source for as many job search platforms as possible, and we're open to any company that wants to join us.

## How does it work?
The following visualisation should give you a better understanding:

![img_7.png](img_7.png)
But there is no better way than to see it in action. Let's take a look at the example of how Gandi works with a company. 

## Non-goals

We aim for ease of use, consistency and transparency, but there are certain areas Gandi explicitly does not target:

1. __To provide a strict copy of the company's original job listing__. Gandi consumers shouldn't act like a job
   application platforms, but rather as unique search engines. We completely accept aggregated information – a result of
   Gandi AI worker __and Contributor__ efforts – until that information is not violating the company's original job
   listing and easy to index dynamically.
2. Monetization of job posts – we don't earn profits from __the data we don't own__.
3. To compete with existing job search platforms. __Gandi is useless in a vacuum__. Our goal is simple – to provide
   information. And our information's goal is to be consumed by as many job search platforms as possible, nobody wins in
   the other case.

## Drawbacks and limitations

While we strive to create an alternative way for the job search process, we acknowledge the potential drawbacks of our
system:

- Companies that have no job listings on their website __won't be able to use Gandi__, as we don't provide any job
  listing creation tools. At least for now;
- Some companies might have restrictions on sharing their job adverts outside their platforms, leading to potential
  legal issues. Such remarks seem strange to us, and we keep blindly follow the assumption that it's in the company's
  interest to get as much vacancy distribution as possible, but in any case – we can get it. We left a company deletion
  request form in the issues template and promise to handle such cases ASAP;
- Gandi accepts English-language job listings only.

[//]: # (## Plans for the Future)

[//]: # (Building on our core principles, we aim to:)

[//]: # ()

[//]: # (- Develop a sophisticated search feature that uses AI to match candidates with jobs.)

[//]: # (- Extend our reach by adding more companies to our platform.)

[//]: # (- Improve the frequency of our syncing process for up-to-date retrievals.)

[//]: # (- Enhance user experience through continuous improvements based on user feedback.)

## FAQ

<details>
<summary><b>How often is data on Gandi updated?</b></summary>
Our platforms sync with company websites daily to ensure the most up-to-date job listings.
</details>
<details>
<summary><b>What kind of companies can post job listings?</b></summary>
Any company, regardless of size or industry, can sync their job listings with Gandi. As of beta launch, we're mostly focusing on startups/mid-size companies, but we're open to any company that wants to join us.
</details>
<details>
<summary><b>Are there any costs associated with using Gandi?</b></summary>
Gandi is a free platform. We believe job information should be as public as possible, without any barriers.
</details>

