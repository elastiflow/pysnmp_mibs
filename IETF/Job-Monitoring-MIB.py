# SNMP MIB module (Job-Monitoring-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/Job-Monitoring-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:42:48 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jobmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1)
)
if mibBuilder.loadTexts:
    jobmonMIB.setRevisions(
        ("1999-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JmUTF8StringTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class JmJobStringTC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class JmNaturalLanguageTagTC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class JmTimeStampTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JmJobSourcePlatformTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("sptUNIX", 3),
          ("sptOS2", 4),
          ("sptPCDOS", 5),
          ("sptNT", 6),
          ("sptMVS", 7),
          ("sptVM", 8),
          ("sptOS400", 9),
          ("sptVMS", 10),
          ("sptWindows", 11),
          ("sptNetWare", 12))
    )



class JmFinishingTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("none", 3),
          ("staple", 4),
          ("punch", 5),
          ("cover", 6),
          ("bind", 7))
    )



class JmPrintQualityTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("draft", 3),
          ("normal", 4),
          ("high", 5))
    )



class JmPrinterResolutionTC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixedLength = 9



class JmTonerEconomyTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("off", 3),
          ("on", 4))
    )



class JmBooleanTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("false", 3),
          ("true", 4))
    )



class JmMediumTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("stationery", 3),
          ("transparency", 4),
          ("envelope", 5),
          ("envelopePlain", 6),
          ("envelopeWindow", 7),
          ("continuousLong", 8),
          ("continuousShort", 9),
          ("tabStock", 10),
          ("multiPartForm", 11),
          ("labels", 12),
          ("multiLayer", 13))
    )



class JmJobCollationTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("uncollatedSheets", 3),
          ("collatedDocuments", 4),
          ("uncollatedDocuments", 5))
    )



class JmJobSubmissionIDTypeTC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1



class JmJobStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("pending", 3),
          ("pendingHeld", 4),
          ("processing", 5),
          ("processingStopped", 6),
          ("canceled", 7),
          ("aborted", 8),
          ("completed", 9))
    )



class JmAttributeTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              110,
              111,
              112,
              113,
              114,
              115,
              130,
              131,
              132,
              150,
              151,
              152,
              170,
              171,
              172,
              173,
              174,
              175,
              190,
              191,
              192,
              193,
              194,
              195)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("jobStateReasons2", 3),
          ("jobStateReasons3", 4),
          ("jobStateReasons4", 5),
          ("processingMessage", 6),
          ("processingMessageNaturalLangTag", 7),
          ("jobCodedCharSet", 8),
          ("jobNaturalLanguageTag", 9),
          ("jobURI", 20),
          ("jobAccountName", 21),
          ("serverAssignedJobName", 22),
          ("jobName", 23),
          ("jobServiceTypes", 24),
          ("jobSourceChannelIndex", 25),
          ("jobSourcePlatformType", 26),
          ("submittingServerName", 27),
          ("submittingApplicationName", 28),
          ("jobOriginatingHost", 29),
          ("deviceNameRequested", 30),
          ("queueNameRequested", 31),
          ("physicalDevice", 32),
          ("numberOfDocuments", 33),
          ("fileName", 34),
          ("documentName", 35),
          ("jobComment", 36),
          ("documentFormatIndex", 37),
          ("documentFormat", 38),
          ("jobPriority", 50),
          ("jobProcessAfterDateAndTime", 51),
          ("jobHold", 52),
          ("jobHoldUntil", 53),
          ("outputBin", 54),
          ("sides", 55),
          ("finishing", 56),
          ("printQualityRequested", 70),
          ("printQualityUsed", 71),
          ("printerResolutionRequested", 72),
          ("printerResolutionUsed", 73),
          ("tonerEcomonyRequested", 74),
          ("tonerEcomonyUsed", 75),
          ("tonerDensityRequested", 76),
          ("tonerDensityUsed", 77),
          ("jobCopiesRequested", 90),
          ("jobCopiesCompleted", 91),
          ("documentCopiesRequested", 92),
          ("documentCopiesCompleted", 93),
          ("jobKOctetsTransferred", 94),
          ("sheetCompletedCopyNumber", 95),
          ("sheetCompletedDocumentNumber", 96),
          ("jobCollationType", 97),
          ("impressionsSpooled", 110),
          ("impressionsSentToDevice", 111),
          ("impressionsInterpreted", 112),
          ("impressionsCompletedCurrentCopy", 113),
          ("fullColorImpressionsCompleted", 114),
          ("highlightColorImpressionsCompleted", 115),
          ("pagesRequested", 130),
          ("pagesCompleted", 131),
          ("pagesCompletedCurrentCopy", 132),
          ("sheetsRequested", 150),
          ("sheetsCompleted", 151),
          ("sheetsCompletedCurrentCopy", 152),
          ("mediumRequested", 170),
          ("mediumConsumed", 171),
          ("colorantRequested", 172),
          ("colorantConsumed", 173),
          ("mediumTypeConsumed", 174),
          ("mediumSizeConsumed", 175),
          ("jobSubmissionToServerTime", 190),
          ("jobSubmissionTime", 191),
          ("jobStartedBeingHeldTime", 192),
          ("jobStartedProcessingTime", 193),
          ("jobCompletionTime", 194),
          ("jobProcessingCPUTime", 195))
    )



class JmJobServiceTypesTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JmJobStateReasons1TC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JmJobStateReasons2TC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JmJobStateReasons3TC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JmJobStateReasons4TC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_JobmonMIBObjects_ObjectIdentity = ObjectIdentity
jobmonMIBObjects = _JobmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1)
)
_JmGeneral_ObjectIdentity = ObjectIdentity
jmGeneral = _JmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1)
)
_JmGeneralTable_Object = MibTable
jmGeneralTable = _JmGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jmGeneralTable.setStatus("current")
_JmGeneralEntry_Object = MibTableRow
jmGeneralEntry = _JmGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1)
)
jmGeneralEntry.setIndexNames(
    (0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"),
)
if mibBuilder.loadTexts:
    jmGeneralEntry.setStatus("current")


class _JmGeneralJobSetIndex_Type(Integer32):
    """Custom type jmGeneralJobSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_JmGeneralJobSetIndex_Type.__name__ = "Integer32"
_JmGeneralJobSetIndex_Object = MibTableColumn
jmGeneralJobSetIndex = _JmGeneralJobSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 1),
    _JmGeneralJobSetIndex_Type()
)
jmGeneralJobSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jmGeneralJobSetIndex.setStatus("current")


class _JmGeneralNumberOfActiveJobs_Type(Integer32):
    """Custom type jmGeneralNumberOfActiveJobs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JmGeneralNumberOfActiveJobs_Type.__name__ = "Integer32"
_JmGeneralNumberOfActiveJobs_Object = MibTableColumn
jmGeneralNumberOfActiveJobs = _JmGeneralNumberOfActiveJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 2),
    _JmGeneralNumberOfActiveJobs_Type()
)
jmGeneralNumberOfActiveJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralNumberOfActiveJobs.setStatus("current")


class _JmGeneralOldestActiveJobIndex_Type(Integer32):
    """Custom type jmGeneralOldestActiveJobIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JmGeneralOldestActiveJobIndex_Type.__name__ = "Integer32"
_JmGeneralOldestActiveJobIndex_Object = MibTableColumn
jmGeneralOldestActiveJobIndex = _JmGeneralOldestActiveJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 3),
    _JmGeneralOldestActiveJobIndex_Type()
)
jmGeneralOldestActiveJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralOldestActiveJobIndex.setStatus("current")


class _JmGeneralNewestActiveJobIndex_Type(Integer32):
    """Custom type jmGeneralNewestActiveJobIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JmGeneralNewestActiveJobIndex_Type.__name__ = "Integer32"
_JmGeneralNewestActiveJobIndex_Object = MibTableColumn
jmGeneralNewestActiveJobIndex = _JmGeneralNewestActiveJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 4),
    _JmGeneralNewestActiveJobIndex_Type()
)
jmGeneralNewestActiveJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralNewestActiveJobIndex.setStatus("current")


class _JmGeneralJobPersistence_Type(Integer32):
    """Custom type jmGeneralJobPersistence based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 2147483647),
    )


_JmGeneralJobPersistence_Type.__name__ = "Integer32"
_JmGeneralJobPersistence_Object = MibTableColumn
jmGeneralJobPersistence = _JmGeneralJobPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 5),
    _JmGeneralJobPersistence_Type()
)
jmGeneralJobPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralJobPersistence.setStatus("current")
if mibBuilder.loadTexts:
    jmGeneralJobPersistence.setUnits("seconds")


class _JmGeneralAttributePersistence_Type(Integer32):
    """Custom type jmGeneralAttributePersistence based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 2147483647),
    )


_JmGeneralAttributePersistence_Type.__name__ = "Integer32"
_JmGeneralAttributePersistence_Object = MibTableColumn
jmGeneralAttributePersistence = _JmGeneralAttributePersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 6),
    _JmGeneralAttributePersistence_Type()
)
jmGeneralAttributePersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralAttributePersistence.setStatus("current")
if mibBuilder.loadTexts:
    jmGeneralAttributePersistence.setUnits("seconds")


class _JmGeneralJobSetName_Type(JmUTF8StringTC):
    """Custom type jmGeneralJobSetName based on JmUTF8StringTC"""
    defaultHexValue = ""

    subtypeSpec = JmUTF8StringTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JmGeneralJobSetName_Type.__name__ = "JmUTF8StringTC"
_JmGeneralJobSetName_Object = MibTableColumn
jmGeneralJobSetName = _JmGeneralJobSetName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 7),
    _JmGeneralJobSetName_Type()
)
jmGeneralJobSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmGeneralJobSetName.setStatus("current")
_JmJobID_ObjectIdentity = ObjectIdentity
jmJobID = _JmJobID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2)
)
_JmJobIDTable_Object = MibTable
jmJobIDTable = _JmJobIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jmJobIDTable.setStatus("current")
_JmJobIDEntry_Object = MibTableRow
jmJobIDEntry = _JmJobIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1)
)
jmJobIDEntry.setIndexNames(
    (0, "Job-Monitoring-MIB", "jmJobSubmissionID"),
)
if mibBuilder.loadTexts:
    jmJobIDEntry.setStatus("current")


class _JmJobSubmissionID_Type(OctetString):
    """Custom type jmJobSubmissionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixedLength = 48


_JmJobSubmissionID_Type.__name__ = "OctetString"
_JmJobSubmissionID_Object = MibTableColumn
jmJobSubmissionID = _JmJobSubmissionID_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 1),
    _JmJobSubmissionID_Type()
)
jmJobSubmissionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jmJobSubmissionID.setStatus("current")


class _JmJobIDJobSetIndex_Type(Integer32):
    """Custom type jmJobIDJobSetIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_JmJobIDJobSetIndex_Type.__name__ = "Integer32"
_JmJobIDJobSetIndex_Object = MibTableColumn
jmJobIDJobSetIndex = _JmJobIDJobSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 2),
    _JmJobIDJobSetIndex_Type()
)
jmJobIDJobSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobIDJobSetIndex.setStatus("current")


class _JmJobIDJobIndex_Type(Integer32):
    """Custom type jmJobIDJobIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JmJobIDJobIndex_Type.__name__ = "Integer32"
_JmJobIDJobIndex_Object = MibTableColumn
jmJobIDJobIndex = _JmJobIDJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 3),
    _JmJobIDJobIndex_Type()
)
jmJobIDJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobIDJobIndex.setStatus("current")
_JmJob_ObjectIdentity = ObjectIdentity
jmJob = _JmJob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3)
)
_JmJobTable_Object = MibTable
jmJobTable = _JmJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jmJobTable.setStatus("current")
_JmJobEntry_Object = MibTableRow
jmJobEntry = _JmJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1)
)
jmJobEntry.setIndexNames(
    (0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"),
    (0, "Job-Monitoring-MIB", "jmJobIndex"),
)
if mibBuilder.loadTexts:
    jmJobEntry.setStatus("current")


class _JmJobIndex_Type(Integer32):
    """Custom type jmJobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JmJobIndex_Type.__name__ = "Integer32"
_JmJobIndex_Object = MibTableColumn
jmJobIndex = _JmJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 1),
    _JmJobIndex_Type()
)
jmJobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jmJobIndex.setStatus("current")


class _JmJobState_Type(JmJobStateTC):
    """Custom type jmJobState based on JmJobStateTC"""
    defaultValue = 2


_JmJobState_Type.__name__ = "JmJobStateTC"
_JmJobState_Object = MibTableColumn
jmJobState = _JmJobState_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 2),
    _JmJobState_Type()
)
jmJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobState.setStatus("current")


class _JmJobStateReasons1_Type(JmJobStateReasons1TC):
    """Custom type jmJobStateReasons1 based on JmJobStateReasons1TC"""
    defaultValue = 0


_JmJobStateReasons1_Type.__name__ = "JmJobStateReasons1TC"
_JmJobStateReasons1_Object = MibTableColumn
jmJobStateReasons1 = _JmJobStateReasons1_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 3),
    _JmJobStateReasons1_Type()
)
jmJobStateReasons1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobStateReasons1.setStatus("current")


class _JmNumberOfInterveningJobs_Type(Integer32):
    """Custom type jmNumberOfInterveningJobs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmNumberOfInterveningJobs_Type.__name__ = "Integer32"
_JmNumberOfInterveningJobs_Object = MibTableColumn
jmNumberOfInterveningJobs = _JmNumberOfInterveningJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 4),
    _JmNumberOfInterveningJobs_Type()
)
jmNumberOfInterveningJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmNumberOfInterveningJobs.setStatus("current")


class _JmJobKOctetsPerCopyRequested_Type(Integer32):
    """Custom type jmJobKOctetsPerCopyRequested based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmJobKOctetsPerCopyRequested_Type.__name__ = "Integer32"
_JmJobKOctetsPerCopyRequested_Object = MibTableColumn
jmJobKOctetsPerCopyRequested = _JmJobKOctetsPerCopyRequested_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 5),
    _JmJobKOctetsPerCopyRequested_Type()
)
jmJobKOctetsPerCopyRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobKOctetsPerCopyRequested.setStatus("current")


class _JmJobKOctetsProcessed_Type(Integer32):
    """Custom type jmJobKOctetsProcessed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmJobKOctetsProcessed_Type.__name__ = "Integer32"
_JmJobKOctetsProcessed_Object = MibTableColumn
jmJobKOctetsProcessed = _JmJobKOctetsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 6),
    _JmJobKOctetsProcessed_Type()
)
jmJobKOctetsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobKOctetsProcessed.setStatus("current")


class _JmJobImpressionsPerCopyRequested_Type(Integer32):
    """Custom type jmJobImpressionsPerCopyRequested based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmJobImpressionsPerCopyRequested_Type.__name__ = "Integer32"
_JmJobImpressionsPerCopyRequested_Object = MibTableColumn
jmJobImpressionsPerCopyRequested = _JmJobImpressionsPerCopyRequested_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 7),
    _JmJobImpressionsPerCopyRequested_Type()
)
jmJobImpressionsPerCopyRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobImpressionsPerCopyRequested.setStatus("current")


class _JmJobImpressionsCompleted_Type(Integer32):
    """Custom type jmJobImpressionsCompleted based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmJobImpressionsCompleted_Type.__name__ = "Integer32"
_JmJobImpressionsCompleted_Object = MibTableColumn
jmJobImpressionsCompleted = _JmJobImpressionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 8),
    _JmJobImpressionsCompleted_Type()
)
jmJobImpressionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobImpressionsCompleted.setStatus("current")


class _JmJobOwner_Type(JmJobStringTC):
    """Custom type jmJobOwner based on JmJobStringTC"""
    defaultHexValue = ""

    subtypeSpec = JmJobStringTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JmJobOwner_Type.__name__ = "JmJobStringTC"
_JmJobOwner_Object = MibTableColumn
jmJobOwner = _JmJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 9),
    _JmJobOwner_Type()
)
jmJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmJobOwner.setStatus("current")
_JmAttribute_ObjectIdentity = ObjectIdentity
jmAttribute = _JmAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4)
)
_JmAttributeTable_Object = MibTable
jmAttributeTable = _JmAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jmAttributeTable.setStatus("current")
_JmAttributeEntry_Object = MibTableRow
jmAttributeEntry = _JmAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1)
)
jmAttributeEntry.setIndexNames(
    (0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"),
    (0, "Job-Monitoring-MIB", "jmJobIndex"),
    (0, "Job-Monitoring-MIB", "jmAttributeTypeIndex"),
    (0, "Job-Monitoring-MIB", "jmAttributeInstanceIndex"),
)
if mibBuilder.loadTexts:
    jmAttributeEntry.setStatus("current")
_JmAttributeTypeIndex_Type = JmAttributeTypeTC
_JmAttributeTypeIndex_Object = MibTableColumn
jmAttributeTypeIndex = _JmAttributeTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 1),
    _JmAttributeTypeIndex_Type()
)
jmAttributeTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jmAttributeTypeIndex.setStatus("current")


class _JmAttributeInstanceIndex_Type(Integer32):
    """Custom type jmAttributeInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_JmAttributeInstanceIndex_Type.__name__ = "Integer32"
_JmAttributeInstanceIndex_Object = MibTableColumn
jmAttributeInstanceIndex = _JmAttributeInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 2),
    _JmAttributeInstanceIndex_Type()
)
jmAttributeInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jmAttributeInstanceIndex.setStatus("current")


class _JmAttributeValueAsInteger_Type(Integer32):
    """Custom type jmAttributeValueAsInteger based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_JmAttributeValueAsInteger_Type.__name__ = "Integer32"
_JmAttributeValueAsInteger_Object = MibTableColumn
jmAttributeValueAsInteger = _JmAttributeValueAsInteger_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 3),
    _JmAttributeValueAsInteger_Type()
)
jmAttributeValueAsInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmAttributeValueAsInteger.setStatus("current")


class _JmAttributeValueAsOctets_Type(OctetString):
    """Custom type jmAttributeValueAsOctets based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JmAttributeValueAsOctets_Type.__name__ = "OctetString"
_JmAttributeValueAsOctets_Object = MibTableColumn
jmAttributeValueAsOctets = _JmAttributeValueAsOctets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 4),
    _JmAttributeValueAsOctets_Type()
)
jmAttributeValueAsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jmAttributeValueAsOctets.setStatus("current")
_JobmonMIBNotifications_ObjectIdentity = ObjectIdentity
jobmonMIBNotifications = _JobmonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 2)
)
_JmMIBConformance_ObjectIdentity = ObjectIdentity
jmMIBConformance = _JmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3)
)
_JmMIBGroups_ObjectIdentity = ObjectIdentity
jmMIBGroups = _JmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2)
)

# Managed Objects groups

jmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 1)
)
jmGeneralGroup.setObjects(
      *(("Job-Monitoring-MIB", "jmGeneralNumberOfActiveJobs"),
        ("Job-Monitoring-MIB", "jmGeneralOldestActiveJobIndex"),
        ("Job-Monitoring-MIB", "jmGeneralNewestActiveJobIndex"),
        ("Job-Monitoring-MIB", "jmGeneralJobPersistence"),
        ("Job-Monitoring-MIB", "jmGeneralAttributePersistence"),
        ("Job-Monitoring-MIB", "jmGeneralJobSetName"))
)
if mibBuilder.loadTexts:
    jmGeneralGroup.setStatus("current")

jmJobIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 2)
)
jmJobIDGroup.setObjects(
      *(("Job-Monitoring-MIB", "jmJobIDJobSetIndex"),
        ("Job-Monitoring-MIB", "jmJobIDJobIndex"))
)
if mibBuilder.loadTexts:
    jmJobIDGroup.setStatus("current")

jmJobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 3)
)
jmJobGroup.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("Job-Monitoring-MIB", "jmNumberOfInterveningJobs"),
        ("Job-Monitoring-MIB", "jmJobKOctetsPerCopyRequested"),
        ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"),
        ("Job-Monitoring-MIB", "jmJobImpressionsPerCopyRequested"),
        ("Job-Monitoring-MIB", "jmJobImpressionsCompleted"),
        ("Job-Monitoring-MIB", "jmJobOwner"))
)
if mibBuilder.loadTexts:
    jmJobGroup.setStatus("current")

jmAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 4)
)
jmAttributeGroup.setObjects(
      *(("Job-Monitoring-MIB", "jmAttributeValueAsInteger"),
        ("Job-Monitoring-MIB", "jmAttributeValueAsOctets"))
)
if mibBuilder.loadTexts:
    jmAttributeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

jmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 1)
)
jmMIBCompliance.setObjects(
      *(("Job-Monitoring-MIB", "jmGeneralGroup"),
        ("Job-Monitoring-MIB", "jmJobIDGroup"),
        ("Job-Monitoring-MIB", "jmJobGroup"),
        ("Job-Monitoring-MIB", "jmAttributeGroup"))
)
if mibBuilder.loadTexts:
    jmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Job-Monitoring-MIB",
    **{"JmUTF8StringTC": JmUTF8StringTC,
       "JmJobStringTC": JmJobStringTC,
       "JmNaturalLanguageTagTC": JmNaturalLanguageTagTC,
       "JmTimeStampTC": JmTimeStampTC,
       "JmJobSourcePlatformTypeTC": JmJobSourcePlatformTypeTC,
       "JmFinishingTC": JmFinishingTC,
       "JmPrintQualityTC": JmPrintQualityTC,
       "JmPrinterResolutionTC": JmPrinterResolutionTC,
       "JmTonerEconomyTC": JmTonerEconomyTC,
       "JmBooleanTC": JmBooleanTC,
       "JmMediumTypeTC": JmMediumTypeTC,
       "JmJobCollationTypeTC": JmJobCollationTypeTC,
       "JmJobSubmissionIDTypeTC": JmJobSubmissionIDTypeTC,
       "JmJobStateTC": JmJobStateTC,
       "JmAttributeTypeTC": JmAttributeTypeTC,
       "JmJobServiceTypesTC": JmJobServiceTypesTC,
       "JmJobStateReasons1TC": JmJobStateReasons1TC,
       "JmJobStateReasons2TC": JmJobStateReasons2TC,
       "JmJobStateReasons3TC": JmJobStateReasons3TC,
       "JmJobStateReasons4TC": JmJobStateReasons4TC,
       "jobmonMIB": jobmonMIB,
       "jobmonMIBObjects": jobmonMIBObjects,
       "jmGeneral": jmGeneral,
       "jmGeneralTable": jmGeneralTable,
       "jmGeneralEntry": jmGeneralEntry,
       "jmGeneralJobSetIndex": jmGeneralJobSetIndex,
       "jmGeneralNumberOfActiveJobs": jmGeneralNumberOfActiveJobs,
       "jmGeneralOldestActiveJobIndex": jmGeneralOldestActiveJobIndex,
       "jmGeneralNewestActiveJobIndex": jmGeneralNewestActiveJobIndex,
       "jmGeneralJobPersistence": jmGeneralJobPersistence,
       "jmGeneralAttributePersistence": jmGeneralAttributePersistence,
       "jmGeneralJobSetName": jmGeneralJobSetName,
       "jmJobID": jmJobID,
       "jmJobIDTable": jmJobIDTable,
       "jmJobIDEntry": jmJobIDEntry,
       "jmJobSubmissionID": jmJobSubmissionID,
       "jmJobIDJobSetIndex": jmJobIDJobSetIndex,
       "jmJobIDJobIndex": jmJobIDJobIndex,
       "jmJob": jmJob,
       "jmJobTable": jmJobTable,
       "jmJobEntry": jmJobEntry,
       "jmJobIndex": jmJobIndex,
       "jmJobState": jmJobState,
       "jmJobStateReasons1": jmJobStateReasons1,
       "jmNumberOfInterveningJobs": jmNumberOfInterveningJobs,
       "jmJobKOctetsPerCopyRequested": jmJobKOctetsPerCopyRequested,
       "jmJobKOctetsProcessed": jmJobKOctetsProcessed,
       "jmJobImpressionsPerCopyRequested": jmJobImpressionsPerCopyRequested,
       "jmJobImpressionsCompleted": jmJobImpressionsCompleted,
       "jmJobOwner": jmJobOwner,
       "jmAttribute": jmAttribute,
       "jmAttributeTable": jmAttributeTable,
       "jmAttributeEntry": jmAttributeEntry,
       "jmAttributeTypeIndex": jmAttributeTypeIndex,
       "jmAttributeInstanceIndex": jmAttributeInstanceIndex,
       "jmAttributeValueAsInteger": jmAttributeValueAsInteger,
       "jmAttributeValueAsOctets": jmAttributeValueAsOctets,
       "jobmonMIBNotifications": jobmonMIBNotifications,
       "jmMIBConformance": jmMIBConformance,
       "jmMIBCompliance": jmMIBCompliance,
       "jmMIBGroups": jmMIBGroups,
       "jmGeneralGroup": jmGeneralGroup,
       "jmJobIDGroup": jmJobIDGroup,
       "jmJobGroup": jmJobGroup,
       "jmAttributeGroup": jmAttributeGroup}
)
