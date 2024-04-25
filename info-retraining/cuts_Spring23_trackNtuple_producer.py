# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase1_2021_realistic -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier DQMIO -n -1 --geometry DB:Extended --era Run3 --eventcontent DQM --no_exec --filein file:/data2/mmasciov/DPNoteMkFit/CMSSW_12_4_0_pre4/src/RelValTTbar_14TeV_CMSSW_12_4_0_pre3-PU_123X_mcRun3_2021_realistic_v14-v1_GEN-SIM-DIGI-RAW_0a130b00-f603-48b4-9c14-3e563b44ca0c.root --fileout step3_mkFit_TTbarPU.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
#from Configuration.Eras.Era_Phase2_cff import Phase2

process = cms.Process('MYRECO', Phase2C17I13M9)
#process = cms.Process('MYRECO',Phase2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.Geometry.GeometryExtended2026D88Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D88_cff')
process.load('Configuration.Geometry.GeometryExtended2026D95Reco_cff')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#process.load('RecoTracker.IterativeTracking.DetachedQuadStep_cff')


import RecoTracker.IterativeTracking.iterativeTkConfig as _cfg
detachedTripletStepClusters = _cfg.clusterRemoverForIter('DetachedTripletStep')

for _eraName, _postfix, _era in _cfg.nonDefaultEras():
    _era.toReplaceWith(detachedTripletStepClusters, _cfg.clusterRemoverForIter('DetachedTripletStep', _eraName, _postfix))

#from RecoLocalMuon.GEMRecHit.gemRecHitsDef_cfi import *
#gemRecHits = gemRecHitsDef.clone(
    #applyMasking = False,
    #maskFile = cms.FileInPath("RecoLocalMuon/GEMRecHit/data/maskedStrips.txt"),
    #deadFile = cms.FileInPath("RecoLocalMuon/GEMRecHit/data/deadStrips.txt")
#    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('root://cms-xcache.rcac.purdue.edu//store/mc/Phase2Spring23DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_131X_mcRun4_realistic_v5-v1/50000/023b71b9-1d38-4891-b5e6-d584032d2cc4.root'),
    #fileNames = cms.untracked.vstring('/store/mc/Phase2Spring23DIGIRECOMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30001/020df31c-aa84-42b3-96d5-df1e4686a198.root'),
    #fileNames = cms.untracked.vstring('/store/mc/Phase2Fall22DRMiniAOD/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0064cbd6-2198-42e7-88f3-149736024681.root'),
    #inputCommands = cms.untracked.vstring('drop *_*_*_HLT'),
    secondaryFileNames = cms.untracked.vstring()
)

    

#from RecoMuon.MuonIdentification.earlyMuons_cfi import earlyMuons
#process.gemRecHits = cms.EDProducer("GEMRecHitProducer",
#    recAlgoConfig = cms.PSet(),
#    recAlgo = cms.string('GEMRecHitStandardAlgo'),
#    gemDigiLabel = cms.InputTag("simMuonGEMDigis"),
#    # maskSource = cms.string('File'),
#    # maskvecfile = cms.FileInPath('RecoLocalMuon/GEMRecHit/data/GEMMaskVec.dat'),
#    # deadSource = cms.string('File'),
#    # deadvecfile = cms.FileInPath('RecoLocalMuon/GEMRecHit/data/GEMDeadVec.dat')
#)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)



# Output definition

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3_mkFit_TTbarPU.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun4_realistic_v5', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '125X_mcRun4_realistic_v2', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
#process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly+process.gemRecHits)
process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
from Validation.RecoTrack.customiseTrackingNtuple import customiseTrackingNtuple
process = customiseTrackingNtuple(process)

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions

#Setup FWK for multithreaded
process.options.numberOfThreads = 4
process.options.numberOfStreams = 0

process.initialStep.qualityCuts = [-100.0, -100.0, -100.0]
process.lowPtQuadStep.qualityCuts = [-100.0, -100.0, -100.0]
process.highPtTripletStep.qualityCuts = [-100.0, -100.0, -100.0]
process.lowPtTripletStep.qualityCuts = [-100.0, -100.0, -100.0]
#process.detachedQuadStep.qualityCuts = [-100.0, -100.0, -100.0]
process.detachedTripletStep.qualityCuts = [-100.0, -100.0, -100.0]
process.pixelPairStep.qualityCuts = [-100.0, -100.0, -100.0]
process.mixedTripletStep.qualityCuts = [-100.0, -100.0, -100.0]
process.pixelLessStep.qualityCuts = [-100.0, -100.0, -100.0]
process.tobTecStep.qualityCuts = [-100.0, -100.0, -100.0]
process.jetCoreRegionalStep.qualityCuts = [-100.0, -100.0, -100.0]
# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
