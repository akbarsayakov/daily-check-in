export default function Home() {
  return (
    <>
      <div className='py-16 md:py-24 lg:py-32 mx-auto w-full max-w-7xl px-5 md:px-10'>
        <div className='grid grid-cols-1 items-center gap-8 sm:gap-20 lg:grid-cols-2'>
          <div className='max-[991px]:max-w-[720px]'>
            <h1 className='mb-4 text-4xl font-bold md:text-6xl'>
              The Website You Want Without The Dev Time.
            </h1>
            <div className='mb-6 max-w-[528px] md:mb-10 lg:mb-12'>
              <p className='text-sm text-[#636262] sm:text-xl'>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit ut
                aliquam, purus sit amet luctus venenatis, lectus
              </p>
            </div>
            <div className='mb-5 md:mb-6 lg:mb-4 pb-8'>form</div>
            <div className="grid grid-flow-row [grid-template:'Area'_/_1fr_1fr_1fr] gap-4">
              <div>
                <h3 className='text-2xl font-bold md:text-3xl'>10K+</h3>
                <p className='text-sm text-[#636262] sm:text-sm'>Customers</p>
              </div>
              <div>
                <h3 className='text-2xl font-bold md:text-3xl'>200K+</h3>
                <p className='text-sm text-[#636262] sm:text-sm'>Emails</p>
              </div>
              <div>
                <h3 className='text-2xl font-bold md:text-3xl'>500+</h3>
                <p className='text-sm text-[#636262] sm:text-sm'>Projects</p>
              </div>
            </div>
          </div>
          <div>Image</div>
        </div>
      </div>
    </>
  )
}
