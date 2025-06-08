# SNMP MIB module (LAN-EMULATION-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/LAN-EMULATION-CLIENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:06:53 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""




class AtmLaneAddress(OctetString):
    """Custom type AtmLaneAddress based on OctetString"""




class VpiInteger(Integer32):
    """Custom type VpiInteger based on Integer32"""




class VciInteger(Integer32):
    """Custom type VciInteger based on Integer32"""




class LeConnectionInterface(Integer32):
    """Custom type LeConnectionInterface based on Integer32"""




class LecState(Integer32):
    """Custom type LecState based on Integer32"""
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
        *(("initialState", 1),
          ("lecsConnect", 2),
          ("configure", 3),
          ("join", 4),
          ("initialRegistration", 5),
          ("busConnect", 6),
          ("operational", 7))
    )





class LecDataFrameFormat(Integer32):
    """Custom type LecDataFrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("aflane8023", 2),
          ("aflane8025", 3))
    )





class LecDataFrameSize(Integer32):
    """Custom type LecDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("max1516", 2),
          ("max4544", 3),
          ("max9234", 4),
          ("max18190", 5),
          ("max1580", 6))
    )





class LeArpTableEntryType(Integer32):
    """Custom type LeArpTableEntryType based on Integer32"""
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
          ("learnedViaControl", 2),
          ("learnedViaData", 3),
          ("staticVolatile", 4),
          ("staticNonVolatile", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfLanEmulation_ObjectIdentity = ObjectIdentity
atmfLanEmulation = _AtmfLanEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3)
)
_LeClientMIB_ObjectIdentity = ObjectIdentity
leClientMIB = _LeClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1)
)
_LeClientMIBObjects_ObjectIdentity = ObjectIdentity
leClientMIBObjects = _LeClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1)
)
_LecConfigTable_Object = MibTable
lecConfigTable = _LecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lecConfigTable.setStatus("mandatory")
_LecConfigEntry_Object = MibTableRow
lecConfigEntry = _LecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1)
)
lecConfigEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecConfigEntry.setStatus("mandatory")
_LecIndex_Type = Integer32
_LecIndex_Object = MibTableColumn
lecIndex = _LecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 1),
    _LecIndex_Type()
)
lecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecIndex.setStatus("mandatory")
_LecRowStatus_Type = RowStatus
_LecRowStatus_Object = MibTableColumn
lecRowStatus = _LecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 2),
    _LecRowStatus_Type()
)
lecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecRowStatus.setStatus("mandatory")
_LecOwner_Type = OwnerString
_LecOwner_Object = MibTableColumn
lecOwner = _LecOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 3),
    _LecOwner_Type()
)
lecOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecOwner.setStatus("mandatory")


class _LecConfigMode_Type(Integer32):
    """Custom type lecConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_LecConfigMode_Type.__name__ = "Integer32"
_LecConfigMode_Object = MibTableColumn
lecConfigMode = _LecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 4),
    _LecConfigMode_Type()
)
lecConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigMode.setStatus("mandatory")


class _LecConfigLanType_Type(LecDataFrameFormat):
    """Custom type lecConfigLanType based on LecDataFrameFormat"""
    defaultValue = 1


_LecConfigLanType_Type.__name__ = "LecDataFrameFormat"
_LecConfigLanType_Object = MibTableColumn
lecConfigLanType = _LecConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 5),
    _LecConfigLanType_Type()
)
lecConfigLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLanType.setStatus("mandatory")


class _LecConfigMaxDataFrameSize_Type(LecDataFrameSize):
    """Custom type lecConfigMaxDataFrameSize based on LecDataFrameSize"""
    defaultValue = 1


_LecConfigMaxDataFrameSize_Type.__name__ = "LecDataFrameSize"
_LecConfigMaxDataFrameSize_Object = MibTableColumn
lecConfigMaxDataFrameSize = _LecConfigMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 6),
    _LecConfigMaxDataFrameSize_Type()
)
lecConfigMaxDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigMaxDataFrameSize.setStatus("mandatory")
_LecConfigLanName_Type = DisplayString
_LecConfigLanName_Object = MibTableColumn
lecConfigLanName = _LecConfigLanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 7),
    _LecConfigLanName_Type()
)
lecConfigLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLanName.setStatus("mandatory")
_LecConfigLesAtmAddress_Type = AtmLaneAddress
_LecConfigLesAtmAddress_Object = MibTableColumn
lecConfigLesAtmAddress = _LecConfigLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 8),
    _LecConfigLesAtmAddress_Type()
)
lecConfigLesAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLesAtmAddress.setStatus("mandatory")


class _LecControlTimeout_Type(Integer32):
    """Custom type lecControlTimeout based on Integer32"""
    defaultValue = 30


_LecControlTimeout_Type.__name__ = "Integer32"
_LecControlTimeout_Object = MibTableColumn
lecControlTimeout = _LecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 9),
    _LecControlTimeout_Type()
)
lecControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecControlTimeout.setStatus("mandatory")


class _LecMaxUnknownFrameCount_Type(Integer32):
    """Custom type lecMaxUnknownFrameCount based on Integer32"""
    defaultValue = 1


_LecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_LecMaxUnknownFrameCount_Object = MibTableColumn
lecMaxUnknownFrameCount = _LecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 10),
    _LecMaxUnknownFrameCount_Type()
)
lecMaxUnknownFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameCount.setStatus("mandatory")


class _LecMaxUnknownFrameTime_Type(Integer32):
    """Custom type lecMaxUnknownFrameTime based on Integer32"""
    defaultValue = 1


_LecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_LecMaxUnknownFrameTime_Object = MibTableColumn
lecMaxUnknownFrameTime = _LecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 11),
    _LecMaxUnknownFrameTime_Type()
)
lecMaxUnknownFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameTime.setStatus("mandatory")


class _LecVccTimeoutPeriod_Type(Integer32):
    """Custom type lecVccTimeoutPeriod based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LecVccTimeoutPeriod_Type.__name__ = "Integer32"
_LecVccTimeoutPeriod_Object = MibTableColumn
lecVccTimeoutPeriod = _LecVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 12),
    _LecVccTimeoutPeriod_Type()
)
lecVccTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecVccTimeoutPeriod.setStatus("mandatory")


class _LecMaxRetryCount_Type(Integer32):
    """Custom type lecMaxRetryCount based on Integer32"""
    defaultValue = 1


_LecMaxRetryCount_Type.__name__ = "Integer32"
_LecMaxRetryCount_Object = MibTableColumn
lecMaxRetryCount = _LecMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 13),
    _LecMaxRetryCount_Type()
)
lecMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxRetryCount.setStatus("mandatory")


class _LecAgingTime_Type(Integer32):
    """Custom type lecAgingTime based on Integer32"""
    defaultValue = 300


_LecAgingTime_Type.__name__ = "Integer32"
_LecAgingTime_Object = MibTableColumn
lecAgingTime = _LecAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 14),
    _LecAgingTime_Type()
)
lecAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecAgingTime.setStatus("mandatory")


class _LecForwardDelayTime_Type(Integer32):
    """Custom type lecForwardDelayTime based on Integer32"""
    defaultValue = 15


_LecForwardDelayTime_Type.__name__ = "Integer32"
_LecForwardDelayTime_Object = MibTableColumn
lecForwardDelayTime = _LecForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 15),
    _LecForwardDelayTime_Type()
)
lecForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecForwardDelayTime.setStatus("mandatory")


class _LecExpectedArpResponseTime_Type(Integer32):
    """Custom type lecExpectedArpResponseTime based on Integer32"""
    defaultValue = 1


_LecExpectedArpResponseTime_Type.__name__ = "Integer32"
_LecExpectedArpResponseTime_Object = MibTableColumn
lecExpectedArpResponseTime = _LecExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 16),
    _LecExpectedArpResponseTime_Type()
)
lecExpectedArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecExpectedArpResponseTime.setStatus("mandatory")


class _LecFlushTimeOut_Type(Integer32):
    """Custom type lecFlushTimeOut based on Integer32"""
    defaultValue = 4


_LecFlushTimeOut_Type.__name__ = "Integer32"
_LecFlushTimeOut_Object = MibTableColumn
lecFlushTimeOut = _LecFlushTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 17),
    _LecFlushTimeOut_Type()
)
lecFlushTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecFlushTimeOut.setStatus("mandatory")


class _LecPathSwitchingDelay_Type(Integer32):
    """Custom type lecPathSwitchingDelay based on Integer32"""
    defaultValue = 6


_LecPathSwitchingDelay_Type.__name__ = "Integer32"
_LecPathSwitchingDelay_Object = MibTableColumn
lecPathSwitchingDelay = _LecPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 18),
    _LecPathSwitchingDelay_Type()
)
lecPathSwitchingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecPathSwitchingDelay.setStatus("mandatory")
_LecLocalSegmentID_Type = Integer32
_LecLocalSegmentID_Object = MibTableColumn
lecLocalSegmentID = _LecLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 19),
    _LecLocalSegmentID_Type()
)
lecLocalSegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLocalSegmentID.setStatus("mandatory")


class _LecMulticastSendType_Type(Integer32):
    """Custom type lecMulticastSendType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("variableBitRate", 2),
          ("constantBitRate", 3))
    )


_LecMulticastSendType_Type.__name__ = "Integer32"
_LecMulticastSendType_Object = MibTableColumn
lecMulticastSendType = _LecMulticastSendType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 20),
    _LecMulticastSendType_Type()
)
lecMulticastSendType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMulticastSendType.setStatus("mandatory")


class _LecMulticastSendAvgRate_Type(Integer32):
    """Custom type lecMulticastSendAvgRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LecMulticastSendAvgRate_Type.__name__ = "Integer32"
_LecMulticastSendAvgRate_Object = MibTableColumn
lecMulticastSendAvgRate = _LecMulticastSendAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 21),
    _LecMulticastSendAvgRate_Type()
)
lecMulticastSendAvgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMulticastSendAvgRate.setStatus("mandatory")


class _LecMulticastSendPeakRate_Type(Integer32):
    """Custom type lecMulticastSendPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LecMulticastSendPeakRate_Type.__name__ = "Integer32"
_LecMulticastSendPeakRate_Object = MibTableColumn
lecMulticastSendPeakRate = _LecMulticastSendPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 22),
    _LecMulticastSendPeakRate_Type()
)
lecMulticastSendPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMulticastSendPeakRate.setStatus("mandatory")


class _LecConnectionCompleteTimer_Type(Integer32):
    """Custom type lecConnectionCompleteTimer based on Integer32"""
    defaultValue = 4


_LecConnectionCompleteTimer_Type.__name__ = "Integer32"
_LecConnectionCompleteTimer_Object = MibTableColumn
lecConnectionCompleteTimer = _LecConnectionCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 23),
    _LecConnectionCompleteTimer_Type()
)
lecConnectionCompleteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConnectionCompleteTimer.setStatus("mandatory")
_LecConfigLecsAtmAddress_Type = AtmLaneAddress
_LecConfigLecsAtmAddress_Object = MibTableColumn
lecConfigLecsAtmAddress = _LecConfigLecsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 24),
    _LecConfigLecsAtmAddress_Type()
)
lecConfigLecsAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLecsAtmAddress.setStatus("mandatory")


class _LecInitialControlTimeout_Type(Integer32):
    """Custom type lecInitialControlTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LecInitialControlTimeout_Type.__name__ = "Integer32"
_LecInitialControlTimeout_Object = MibTableColumn
lecInitialControlTimeout = _LecInitialControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 25),
    _LecInitialControlTimeout_Type()
)
lecInitialControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecInitialControlTimeout.setStatus("mandatory")


class _LecControlTimeoutMultiplier_Type(Integer32):
    """Custom type lecControlTimeoutMultiplier based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_LecControlTimeoutMultiplier_Type.__name__ = "Integer32"
_LecControlTimeoutMultiplier_Object = MibTableColumn
lecControlTimeoutMultiplier = _LecControlTimeoutMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 26),
    _LecControlTimeoutMultiplier_Type()
)
lecControlTimeoutMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecControlTimeoutMultiplier.setStatus("mandatory")


class _LecV2MaxUnknownFrameCount_Type(Integer32):
    """Custom type lecV2MaxUnknownFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_LecV2MaxUnknownFrameCount_Type.__name__ = "Integer32"
_LecV2MaxUnknownFrameCount_Object = MibTableColumn
lecV2MaxUnknownFrameCount = _LecV2MaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 27),
    _LecV2MaxUnknownFrameCount_Type()
)
lecV2MaxUnknownFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecV2MaxUnknownFrameCount.setStatus("mandatory")


class _LecConfigLocalSegmentID_Type(Integer32):
    """Custom type lecConfigLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecConfigLocalSegmentID_Type.__name__ = "Integer32"
_LecConfigLocalSegmentID_Object = MibTableColumn
lecConfigLocalSegmentID = _LecConfigLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 28),
    _LecConfigLocalSegmentID_Type()
)
lecConfigLocalSegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLocalSegmentID.setStatus("mandatory")
_LecConfigV2Capable_Type = TruthValue
_LecConfigV2Capable_Object = MibTableColumn
lecConfigV2Capable = _LecConfigV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 29),
    _LecConfigV2Capable_Type()
)
lecConfigV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigV2Capable.setStatus("mandatory")
_LecConfigSelectiveMulticast_Type = TruthValue
_LecConfigSelectiveMulticast_Object = MibTableColumn
lecConfigSelectiveMulticast = _LecConfigSelectiveMulticast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 30),
    _LecConfigSelectiveMulticast_Type()
)
lecConfigSelectiveMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigSelectiveMulticast.setStatus("mandatory")


class _LecForwardDisconnectTimeout_Type(Integer32):
    """Custom type lecForwardDisconnectTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LecForwardDisconnectTimeout_Type.__name__ = "Integer32"
_LecForwardDisconnectTimeout_Object = MibTableColumn
lecForwardDisconnectTimeout = _LecForwardDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 31),
    _LecForwardDisconnectTimeout_Type()
)
lecForwardDisconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecForwardDisconnectTimeout.setStatus("mandatory")
_LecConfigLLCMultiplexCapable_Type = TruthValue
_LecConfigLLCMultiplexCapable_Object = MibTableColumn
lecConfigLLCMultiplexCapable = _LecConfigLLCMultiplexCapable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 32),
    _LecConfigLLCMultiplexCapable_Type()
)
lecConfigLLCMultiplexCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecConfigLLCMultiplexCapable.setStatus("mandatory")


class _LecMinReconfigureDelay_Type(Integer32):
    """Custom type lecMinReconfigureDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_LecMinReconfigureDelay_Type.__name__ = "Integer32"
_LecMinReconfigureDelay_Object = MibTableColumn
lecMinReconfigureDelay = _LecMinReconfigureDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 33),
    _LecMinReconfigureDelay_Type()
)
lecMinReconfigureDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMinReconfigureDelay.setStatus("mandatory")


class _LecMaxReconfigureDelay_Type(Integer32):
    """Custom type lecMaxReconfigureDelay based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_LecMaxReconfigureDelay_Type.__name__ = "Integer32"
_LecMaxReconfigureDelay_Object = MibTableColumn
lecMaxReconfigureDelay = _LecMaxReconfigureDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 34),
    _LecMaxReconfigureDelay_Type()
)
lecMaxReconfigureDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxReconfigureDelay.setStatus("mandatory")


class _LecMaxBusConnectRetries_Type(Integer32):
    """Custom type lecMaxBusConnectRetries based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LecMaxBusConnectRetries_Type.__name__ = "Integer32"
_LecMaxBusConnectRetries_Object = MibTableColumn
lecMaxBusConnectRetries = _LecMaxBusConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 35),
    _LecMaxBusConnectRetries_Type()
)
lecMaxBusConnectRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxBusConnectRetries.setStatus("mandatory")
_LecTokenRingExplorerExclude_Type = TruthValue
_LecTokenRingExplorerExclude_Object = MibTableColumn
lecTokenRingExplorerExclude = _LecTokenRingExplorerExclude_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 36),
    _LecTokenRingExplorerExclude_Type()
)
lecTokenRingExplorerExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecTokenRingExplorerExclude.setStatus("mandatory")
_LecStatusTable_Object = MibTable
lecStatusTable = _LecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lecStatusTable.setStatus("mandatory")
_LecStatusEntry_Object = MibTableRow
lecStatusEntry = _LecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1)
)
lecStatusEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIfIndex"),
)
if mibBuilder.loadTexts:
    lecStatusEntry.setStatus("mandatory")


class _LecIfIndex_Type(Integer32):
    """Custom type lecIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LecIfIndex_Type.__name__ = "Integer32"
_LecIfIndex_Object = MibTableColumn
lecIfIndex = _LecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 1),
    _LecIfIndex_Type()
)
lecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecIfIndex.setStatus("mandatory")
_LecPrimaryAtmAddress_Type = AtmLaneAddress
_LecPrimaryAtmAddress_Object = MibTableColumn
lecPrimaryAtmAddress = _LecPrimaryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 2),
    _LecPrimaryAtmAddress_Type()
)
lecPrimaryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecPrimaryAtmAddress.setStatus("mandatory")
_LecID_Type = Integer32
_LecID_Object = MibTableColumn
lecID = _LecID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 3),
    _LecID_Type()
)
lecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecID.setStatus("mandatory")
_LecInterfaceState_Type = LecState
_LecInterfaceState_Object = MibTableColumn
lecInterfaceState = _LecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 4),
    _LecInterfaceState_Type()
)
lecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecInterfaceState.setStatus("mandatory")


class _LecLastFailureRespCode_Type(Integer32):
    """Custom type lecLastFailureRespCode based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4),
          ("invalidRequestParameters", 5),
          ("duplicateLanDestination", 6),
          ("duplicateAtmAddress", 7),
          ("insufficientResources", 8),
          ("accessDenied", 9),
          ("invalidRequesterId", 10),
          ("invalidLanDestination", 11),
          ("invalidAtmAddress", 12),
          ("noConfiguration", 13),
          ("leConfigureError", 14),
          ("insufficientInformation", 15),
          ("tlvNotFound", 16))
    )


_LecLastFailureRespCode_Type.__name__ = "Integer32"
_LecLastFailureRespCode_Object = MibTableColumn
lecLastFailureRespCode = _LecLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 5),
    _LecLastFailureRespCode_Type()
)
lecLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureRespCode.setStatus("mandatory")
_LecLastFailureState_Type = LecState
_LecLastFailureState_Object = MibTableColumn
lecLastFailureState = _LecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 6),
    _LecLastFailureState_Type()
)
lecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureState.setStatus("mandatory")
_LecProtocol_Type = Integer32
_LecProtocol_Object = MibTableColumn
lecProtocol = _LecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 7),
    _LecProtocol_Type()
)
lecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecProtocol.setStatus("mandatory")
_LecVersion_Type = Integer32
_LecVersion_Object = MibTableColumn
lecVersion = _LecVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 8),
    _LecVersion_Type()
)
lecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecVersion.setStatus("mandatory")
_LecTopologyChange_Type = TruthValue
_LecTopologyChange_Object = MibTableColumn
lecTopologyChange = _LecTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 9),
    _LecTopologyChange_Type()
)
lecTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecTopologyChange.setStatus("mandatory")
_LecConfigServerAtmAddress_Type = AtmLaneAddress
_LecConfigServerAtmAddress_Object = MibTableColumn
lecConfigServerAtmAddress = _LecConfigServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 10),
    _LecConfigServerAtmAddress_Type()
)
lecConfigServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigServerAtmAddress.setStatus("mandatory")


class _LecConfigSource_Type(Integer32):
    """Custom type lecConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gotAddressViaIlmi", 1),
          ("usedWellKnownAddress", 2),
          ("usedLecsPvc", 3),
          ("didNotUseLecs", 4),
          ("usedConfiguredAddress", 5),
          ("configInProgress", 6))
    )


_LecConfigSource_Type.__name__ = "Integer32"
_LecConfigSource_Object = MibTableColumn
lecConfigSource = _LecConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 11),
    _LecConfigSource_Type()
)
lecConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigSource.setStatus("mandatory")
_LecActualLanType_Type = LecDataFrameFormat
_LecActualLanType_Object = MibTableColumn
lecActualLanType = _LecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 12),
    _LecActualLanType_Type()
)
lecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanType.setStatus("mandatory")
_LecActualMaxDataFrameSize_Type = LecDataFrameSize
_LecActualMaxDataFrameSize_Object = MibTableColumn
lecActualMaxDataFrameSize = _LecActualMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 13),
    _LecActualMaxDataFrameSize_Type()
)
lecActualMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualMaxDataFrameSize.setStatus("mandatory")
_LecActualLanName_Type = DisplayString
_LecActualLanName_Object = MibTableColumn
lecActualLanName = _LecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 14),
    _LecActualLanName_Type()
)
lecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanName.setStatus("mandatory")
_LecActualLesAtmAddress_Type = AtmLaneAddress
_LecActualLesAtmAddress_Object = MibTableColumn
lecActualLesAtmAddress = _LecActualLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 15),
    _LecActualLesAtmAddress_Type()
)
lecActualLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLesAtmAddress.setStatus("mandatory")
_LecProxyClient_Type = TruthValue
_LecProxyClient_Object = MibTableColumn
lecProxyClient = _LecProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 16),
    _LecProxyClient_Type()
)
lecProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecProxyClient.setStatus("mandatory")


class _LecActualLocalSegmentID_Type(Integer32):
    """Custom type lecActualLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecActualLocalSegmentID_Type.__name__ = "Integer32"
_LecActualLocalSegmentID_Object = MibTableColumn
lecActualLocalSegmentID = _LecActualLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 17),
    _LecActualLocalSegmentID_Type()
)
lecActualLocalSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLocalSegmentID.setStatus("mandatory")
_LecActualV2Capable_Type = TruthValue
_LecActualV2Capable_Object = MibTableColumn
lecActualV2Capable = _LecActualV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 18),
    _LecActualV2Capable_Type()
)
lecActualV2Capable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualV2Capable.setStatus("mandatory")


class _LecElanID_Type(Integer32):
    """Custom type lecElanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LecElanID_Type.__name__ = "Integer32"
_LecElanID_Object = MibTableColumn
lecElanID = _LecElanID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 19),
    _LecElanID_Type()
)
lecElanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecElanID.setStatus("mandatory")
_LecActualSelectiveMulticast_Type = TruthValue
_LecActualSelectiveMulticast_Object = MibTableColumn
lecActualSelectiveMulticast = _LecActualSelectiveMulticast_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 20),
    _LecActualSelectiveMulticast_Type()
)
lecActualSelectiveMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualSelectiveMulticast.setStatus("mandatory")
_LecActualLLCMultiplexCapable_Type = TruthValue
_LecActualLLCMultiplexCapable_Object = MibTableColumn
lecActualLLCMultiplexCapable = _LecActualLLCMultiplexCapable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 21),
    _LecActualLLCMultiplexCapable_Type()
)
lecActualLLCMultiplexCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLLCMultiplexCapable.setStatus("mandatory")
_LecPreferredLesAddress_Type = AtmLaneAddress
_LecPreferredLesAddress_Object = MibTableColumn
lecPreferredLesAddress = _LecPreferredLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 22),
    _LecPreferredLesAddress_Type()
)
lecPreferredLesAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecPreferredLesAddress.setStatus("mandatory")
_LecStoresServiceCategories_Type = TruthValue
_LecStoresServiceCategories_Object = MibTableColumn
lecStoresServiceCategories = _LecStoresServiceCategories_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 23),
    _LecStoresServiceCategories_Type()
)
lecStoresServiceCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecStoresServiceCategories.setStatus("mandatory")
_LecMappingTable_Object = MibTable
lecMappingTable = _LecMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lecMappingTable.setStatus("mandatory")
_LecMappingEntry_Object = MibTableRow
lecMappingEntry = _LecMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3, 1)
)
lecMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lecMappingEntry.setStatus("mandatory")
_LecMappingIndex_Type = Integer32
_LecMappingIndex_Object = MibTableColumn
lecMappingIndex = _LecMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3, 1, 1),
    _LecMappingIndex_Type()
)
lecMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMappingIndex.setStatus("mandatory")
_LecStatisticsTable_Object = MibTable
lecStatisticsTable = _LecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lecStatisticsTable.setStatus("mandatory")
_LecStatisticsEntry_Object = MibTableRow
lecStatisticsEntry = _LecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1)
)
lecStatisticsEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecStatisticsEntry.setStatus("mandatory")
_LecArpRequestsOut_Type = Counter32
_LecArpRequestsOut_Object = MibTableColumn
lecArpRequestsOut = _LecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 1),
    _LecArpRequestsOut_Type()
)
lecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsOut.setStatus("mandatory")
_LecArpRequestsIn_Type = Counter32
_LecArpRequestsIn_Object = MibTableColumn
lecArpRequestsIn = _LecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 2),
    _LecArpRequestsIn_Type()
)
lecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsIn.setStatus("mandatory")
_LecArpRepliesOut_Type = Counter32
_LecArpRepliesOut_Object = MibTableColumn
lecArpRepliesOut = _LecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 3),
    _LecArpRepliesOut_Type()
)
lecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesOut.setStatus("mandatory")
_LecArpRepliesIn_Type = Counter32
_LecArpRepliesIn_Object = MibTableColumn
lecArpRepliesIn = _LecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 4),
    _LecArpRepliesIn_Type()
)
lecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesIn.setStatus("mandatory")
_LecControlFramesOut_Type = Counter32
_LecControlFramesOut_Object = MibTableColumn
lecControlFramesOut = _LecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 5),
    _LecControlFramesOut_Type()
)
lecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesOut.setStatus("mandatory")
_LecControlFramesIn_Type = Counter32
_LecControlFramesIn_Object = MibTableColumn
lecControlFramesIn = _LecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 6),
    _LecControlFramesIn_Type()
)
lecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesIn.setStatus("mandatory")
_LecSvcFailures_Type = Counter32
_LecSvcFailures_Object = MibTableColumn
lecSvcFailures = _LecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 7),
    _LecSvcFailures_Type()
)
lecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecSvcFailures.setStatus("mandatory")
_LecFlowFailures_Type = Counter32
_LecFlowFailures_Object = MibTableColumn
lecFlowFailures = _LecFlowFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 8),
    _LecFlowFailures_Type()
)
lecFlowFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecFlowFailures.setStatus("mandatory")
_LecEchoDiscards_Type = Counter32
_LecEchoDiscards_Object = MibTableColumn
lecEchoDiscards = _LecEchoDiscards_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 9),
    _LecEchoDiscards_Type()
)
lecEchoDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecEchoDiscards.setStatus("mandatory")
_LecFilteredMulticasts_Type = Counter32
_LecFilteredMulticasts_Object = MibTableColumn
lecFilteredMulticasts = _LecFilteredMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 10),
    _LecFilteredMulticasts_Type()
)
lecFilteredMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecFilteredMulticasts.setStatus("mandatory")
_LecServerVccTable_Object = MibTable
lecServerVccTable = _LecServerVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lecServerVccTable.setStatus("mandatory")
_LecServerVccEntry_Object = MibTableRow
lecServerVccEntry = _LecServerVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1)
)
lecServerVccEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecServerVccEntry.setStatus("mandatory")
_LecConfigDirectInterface_Type = LeConnectionInterface
_LecConfigDirectInterface_Object = MibTableColumn
lecConfigDirectInterface = _LecConfigDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 1),
    _LecConfigDirectInterface_Type()
)
lecConfigDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectInterface.setStatus("mandatory")
_LecConfigDirectVpi_Type = VpiInteger
_LecConfigDirectVpi_Object = MibTableColumn
lecConfigDirectVpi = _LecConfigDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 2),
    _LecConfigDirectVpi_Type()
)
lecConfigDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectVpi.setStatus("mandatory")
_LecConfigDirectVci_Type = VciInteger
_LecConfigDirectVci_Object = MibTableColumn
lecConfigDirectVci = _LecConfigDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 3),
    _LecConfigDirectVci_Type()
)
lecConfigDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectVci.setStatus("mandatory")
_LecControlDirectInterface_Type = LeConnectionInterface
_LecControlDirectInterface_Object = MibTableColumn
lecControlDirectInterface = _LecControlDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 4),
    _LecControlDirectInterface_Type()
)
lecControlDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectInterface.setStatus("mandatory")
_LecControlDirectVpi_Type = VpiInteger
_LecControlDirectVpi_Object = MibTableColumn
lecControlDirectVpi = _LecControlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 5),
    _LecControlDirectVpi_Type()
)
lecControlDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectVpi.setStatus("mandatory")
_LecControlDirectVci_Type = VciInteger
_LecControlDirectVci_Object = MibTableColumn
lecControlDirectVci = _LecControlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 6),
    _LecControlDirectVci_Type()
)
lecControlDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectVci.setStatus("mandatory")
_LecControlDistributeInterface_Type = LeConnectionInterface
_LecControlDistributeInterface_Object = MibTableColumn
lecControlDistributeInterface = _LecControlDistributeInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 7),
    _LecControlDistributeInterface_Type()
)
lecControlDistributeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeInterface.setStatus("mandatory")
_LecControlDistributeVpi_Type = VpiInteger
_LecControlDistributeVpi_Object = MibTableColumn
lecControlDistributeVpi = _LecControlDistributeVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 8),
    _LecControlDistributeVpi_Type()
)
lecControlDistributeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeVpi.setStatus("mandatory")
_LecControlDistributeVci_Type = VciInteger
_LecControlDistributeVci_Object = MibTableColumn
lecControlDistributeVci = _LecControlDistributeVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 9),
    _LecControlDistributeVci_Type()
)
lecControlDistributeVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeVci.setStatus("mandatory")
_LecMulticastSendInterface_Type = LeConnectionInterface
_LecMulticastSendInterface_Object = MibTableColumn
lecMulticastSendInterface = _LecMulticastSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 10),
    _LecMulticastSendInterface_Type()
)
lecMulticastSendInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendInterface.setStatus("mandatory")
_LecMulticastSendVpi_Type = VpiInteger
_LecMulticastSendVpi_Object = MibTableColumn
lecMulticastSendVpi = _LecMulticastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 11),
    _LecMulticastSendVpi_Type()
)
lecMulticastSendVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendVpi.setStatus("mandatory")
_LecMulticastSendVci_Type = VciInteger
_LecMulticastSendVci_Object = MibTableColumn
lecMulticastSendVci = _LecMulticastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 12),
    _LecMulticastSendVci_Type()
)
lecMulticastSendVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendVci.setStatus("mandatory")
_LecMulticastForwardInterface_Type = LeConnectionInterface
_LecMulticastForwardInterface_Object = MibTableColumn
lecMulticastForwardInterface = _LecMulticastForwardInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 13),
    _LecMulticastForwardInterface_Type()
)
lecMulticastForwardInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardInterface.setStatus("mandatory")
_LecMulticastForwardVpi_Type = VpiInteger
_LecMulticastForwardVpi_Object = MibTableColumn
lecMulticastForwardVpi = _LecMulticastForwardVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 14),
    _LecMulticastForwardVpi_Type()
)
lecMulticastForwardVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardVpi.setStatus("mandatory")
_LecMulticastForwardVci_Type = VciInteger
_LecMulticastForwardVci_Object = MibTableColumn
lecMulticastForwardVci = _LecMulticastForwardVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 15),
    _LecMulticastForwardVci_Type()
)
lecMulticastForwardVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardVci.setStatus("mandatory")
_LecAtmAddressTable_Object = MibTable
lecAtmAddressTable = _LecAtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lecAtmAddressTable.setStatus("mandatory")
_LecAtmAddressEntry_Object = MibTableRow
lecAtmAddressEntry = _LecAtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1)
)
lecAtmAddressEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecAtmAddress"),
)
if mibBuilder.loadTexts:
    lecAtmAddressEntry.setStatus("mandatory")
_LecAtmAddress_Type = AtmLaneAddress
_LecAtmAddress_Object = MibTableColumn
lecAtmAddress = _LecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1, 1),
    _LecAtmAddress_Type()
)
lecAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecAtmAddress.setStatus("mandatory")
_LecAtmAddressStatus_Type = Integer32
_LecAtmAddressStatus_Object = MibTableColumn
lecAtmAddressStatus = _LecAtmAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1, 2),
    _LecAtmAddressStatus_Type()
)
lecAtmAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecAtmAddressStatus.setStatus("mandatory")


class _LecAtmAddressMuxed_Type(Integer32):
    """Custom type lecAtmAddressMuxed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("muxed", 1),
          ("notMuxed", 2),
          ("both", 3),
          ("none", 4))
    )


_LecAtmAddressMuxed_Type.__name__ = "Integer32"
_LecAtmAddressMuxed_Object = MibTableColumn
lecAtmAddressMuxed = _LecAtmAddressMuxed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1, 3),
    _LecAtmAddressMuxed_Type()
)
lecAtmAddressMuxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecAtmAddressMuxed.setStatus("mandatory")
_LecMacAddressTable_Object = MibTable
lecMacAddressTable = _LecMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lecMacAddressTable.setStatus("mandatory")
_LecMacAddressEntry_Object = MibTableRow
lecMacAddressEntry = _LecMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1)
)
lecMacAddressEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecMacAddress"),
)
if mibBuilder.loadTexts:
    lecMacAddressEntry.setStatus("mandatory")
_LecMacAddress_Type = MacAddress
_LecMacAddress_Object = MibTableColumn
lecMacAddress = _LecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 1),
    _LecMacAddress_Type()
)
lecMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecMacAddress.setStatus("mandatory")
_LecMacAddressAtmBinding_Type = AtmLaneAddress
_LecMacAddressAtmBinding_Object = MibTableColumn
lecMacAddressAtmBinding = _LecMacAddressAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 2),
    _LecMacAddressAtmBinding_Type()
)
lecMacAddressAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacAddressAtmBinding.setStatus("mandatory")
_LecMacAddressMuxedAtmBinding_Type = AtmLaneAddress
_LecMacAddressMuxedAtmBinding_Object = MibTableColumn
lecMacAddressMuxedAtmBinding = _LecMacAddressMuxedAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 3),
    _LecMacAddressMuxedAtmBinding_Type()
)
lecMacAddressMuxedAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacAddressMuxedAtmBinding.setStatus("mandatory")


class _LecMacAddressServiceCategory_Type(Integer32):
    """Custom type lecMacAddressServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecMacAddressServiceCategory_Type.__name__ = "Integer32"
_LecMacAddressServiceCategory_Object = MibTableColumn
lecMacAddressServiceCategory = _LecMacAddressServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 4),
    _LecMacAddressServiceCategory_Type()
)
lecMacAddressServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacAddressServiceCategory.setStatus("mandatory")
_LecRouteDescrTable_Object = MibTable
lecRouteDescrTable = _LecRouteDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    lecRouteDescrTable.setStatus("mandatory")
_LecRouteDescrEntry_Object = MibTableRow
lecRouteDescrEntry = _LecRouteDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1)
)
lecRouteDescrEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecRouteDescrSegmentID"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecRouteDescrBridgeNumber"),
)
if mibBuilder.loadTexts:
    lecRouteDescrEntry.setStatus("mandatory")
_LecRouteDescrSegmentID_Type = Integer32
_LecRouteDescrSegmentID_Object = MibTableColumn
lecRouteDescrSegmentID = _LecRouteDescrSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 1),
    _LecRouteDescrSegmentID_Type()
)
lecRouteDescrSegmentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecRouteDescrSegmentID.setStatus("mandatory")
_LecRouteDescrBridgeNumber_Type = Integer32
_LecRouteDescrBridgeNumber_Object = MibTableColumn
lecRouteDescrBridgeNumber = _LecRouteDescrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 2),
    _LecRouteDescrBridgeNumber_Type()
)
lecRouteDescrBridgeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecRouteDescrBridgeNumber.setStatus("mandatory")
_LecRouteDescrAtmBinding_Type = AtmLaneAddress
_LecRouteDescrAtmBinding_Object = MibTableColumn
lecRouteDescrAtmBinding = _LecRouteDescrAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 3),
    _LecRouteDescrAtmBinding_Type()
)
lecRouteDescrAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRouteDescrAtmBinding.setStatus("mandatory")
_LecRouteDescrMuxedAtmBinding_Type = AtmLaneAddress
_LecRouteDescrMuxedAtmBinding_Object = MibTableColumn
lecRouteDescrMuxedAtmBinding = _LecRouteDescrMuxedAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 4),
    _LecRouteDescrMuxedAtmBinding_Type()
)
lecRouteDescrMuxedAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRouteDescrMuxedAtmBinding.setStatus("mandatory")


class _LecRouteDescrServiceCategory_Type(Integer32):
    """Custom type lecRouteDescrServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecRouteDescrServiceCategory_Type.__name__ = "Integer32"
_LecRouteDescrServiceCategory_Object = MibTableColumn
lecRouteDescrServiceCategory = _LecRouteDescrServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 5),
    _LecRouteDescrServiceCategory_Type()
)
lecRouteDescrServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRouteDescrServiceCategory.setStatus("mandatory")
_LeArpTable_Object = MibTable
leArpTable = _LeArpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    leArpTable.setStatus("mandatory")
_LeArpEntry_Object = MibTableRow
leArpEntry = _LeArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1)
)
leArpEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leArpMacAddress"),
)
if mibBuilder.loadTexts:
    leArpEntry.setStatus("mandatory")
_LeArpMacAddress_Type = MacAddress
_LeArpMacAddress_Object = MibTableColumn
leArpMacAddress = _LeArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 1),
    _LeArpMacAddress_Type()
)
leArpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leArpMacAddress.setStatus("mandatory")
_LeArpAtmAddress_Type = AtmLaneAddress
_LeArpAtmAddress_Object = MibTableColumn
leArpAtmAddress = _LeArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 2),
    _LeArpAtmAddress_Type()
)
leArpAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leArpAtmAddress.setStatus("mandatory")
_LeArpIsRemoteAddress_Type = TruthValue
_LeArpIsRemoteAddress_Object = MibTableColumn
leArpIsRemoteAddress = _LeArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 3),
    _LeArpIsRemoteAddress_Type()
)
leArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leArpIsRemoteAddress.setStatus("mandatory")


class _LeArpEntryType_Type(LeArpTableEntryType):
    """Custom type leArpEntryType based on LeArpTableEntryType"""
    defaultValue = 4


_LeArpEntryType_Type.__name__ = "LeArpTableEntryType"
_LeArpEntryType_Object = MibTableColumn
leArpEntryType = _LeArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 4),
    _LeArpEntryType_Type()
)
leArpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leArpEntryType.setStatus("mandatory")
_LeArpRowStatus_Type = RowStatus
_LeArpRowStatus_Object = MibTableColumn
leArpRowStatus = _LeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 5),
    _LeArpRowStatus_Type()
)
leArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leArpRowStatus.setStatus("mandatory")
_LeArpMuxedAtmAddress_Type = AtmLaneAddress
_LeArpMuxedAtmAddress_Object = MibTableColumn
leArpMuxedAtmAddress = _LeArpMuxedAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 6),
    _LeArpMuxedAtmAddress_Type()
)
leArpMuxedAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leArpMuxedAtmAddress.setStatus("mandatory")


class _LeArpServiceCategory_Type(Integer32):
    """Custom type leArpServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LeArpServiceCategory_Type.__name__ = "Integer32"
_LeArpServiceCategory_Object = MibTableColumn
leArpServiceCategory = _LeArpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 7),
    _LeArpServiceCategory_Type()
)
leArpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leArpServiceCategory.setStatus("mandatory")
_LeRDArpTable_Object = MibTable
leRDArpTable = _LeRDArpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    leRDArpTable.setStatus("mandatory")
_LeRDArpEntry_Object = MibTableRow
leRDArpEntry = _LeRDArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1)
)
leRDArpEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leRDArpSegmentID"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leRDArpBridgeNumber"),
)
if mibBuilder.loadTexts:
    leRDArpEntry.setStatus("mandatory")
_LeRDArpSegmentID_Type = Integer32
_LeRDArpSegmentID_Object = MibTableColumn
leRDArpSegmentID = _LeRDArpSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 1),
    _LeRDArpSegmentID_Type()
)
leRDArpSegmentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leRDArpSegmentID.setStatus("mandatory")
_LeRDArpBridgeNumber_Type = Integer32
_LeRDArpBridgeNumber_Object = MibTableColumn
leRDArpBridgeNumber = _LeRDArpBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 2),
    _LeRDArpBridgeNumber_Type()
)
leRDArpBridgeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leRDArpBridgeNumber.setStatus("mandatory")
_LeRDArpAtmAddress_Type = AtmLaneAddress
_LeRDArpAtmAddress_Object = MibTableColumn
leRDArpAtmAddress = _LeRDArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 3),
    _LeRDArpAtmAddress_Type()
)
leRDArpAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leRDArpAtmAddress.setStatus("mandatory")


class _LeRDArpEntryType_Type(LeArpTableEntryType):
    """Custom type leRDArpEntryType based on LeArpTableEntryType"""
    defaultValue = 4


_LeRDArpEntryType_Type.__name__ = "LeArpTableEntryType"
_LeRDArpEntryType_Object = MibTableColumn
leRDArpEntryType = _LeRDArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 4),
    _LeRDArpEntryType_Type()
)
leRDArpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leRDArpEntryType.setStatus("mandatory")
_LeRDArpRowStatus_Type = RowStatus
_LeRDArpRowStatus_Object = MibTableColumn
leRDArpRowStatus = _LeRDArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 5),
    _LeRDArpRowStatus_Type()
)
leRDArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leRDArpRowStatus.setStatus("mandatory")
_LeRDArpMuxedAtmAddress_Type = AtmLaneAddress
_LeRDArpMuxedAtmAddress_Object = MibTableColumn
leRDArpMuxedAtmAddress = _LeRDArpMuxedAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 6),
    _LeRDArpMuxedAtmAddress_Type()
)
leRDArpMuxedAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leRDArpMuxedAtmAddress.setStatus("mandatory")


class _LeRDArpServiceCategory_Type(Integer32):
    """Custom type leRDArpServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LeRDArpServiceCategory_Type.__name__ = "Integer32"
_LeRDArpServiceCategory_Object = MibTableColumn
leRDArpServiceCategory = _LeRDArpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 7),
    _LeRDArpServiceCategory_Type()
)
leRDArpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leRDArpServiceCategory.setStatus("mandatory")
_LeRDArpIsRemoteDescriptor_Type = TruthValue
_LeRDArpIsRemoteDescriptor_Object = MibTableColumn
leRDArpIsRemoteDescriptor = _LeRDArpIsRemoteDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 8),
    _LeRDArpIsRemoteDescriptor_Type()
)
leRDArpIsRemoteDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leRDArpIsRemoteDescriptor.setStatus("mandatory")
_LecMcForwardTable_Object = MibTable
lecMcForwardTable = _LecMcForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    lecMcForwardTable.setStatus("mandatory")
_LecMcForwardEntry_Object = MibTableRow
lecMcForwardEntry = _LecMcForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11, 1)
)
lecMcForwardEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecMcForwardInterface"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecMcForwardVpi"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecMcForwardVci"),
)
if mibBuilder.loadTexts:
    lecMcForwardEntry.setStatus("mandatory")
_LecMcForwardInterface_Type = LeConnectionInterface
_LecMcForwardInterface_Object = MibTableColumn
lecMcForwardInterface = _LecMcForwardInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11, 1, 1),
    _LecMcForwardInterface_Type()
)
lecMcForwardInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecMcForwardInterface.setStatus("mandatory")
_LecMcForwardVpi_Type = VpiInteger
_LecMcForwardVpi_Object = MibTableColumn
lecMcForwardVpi = _LecMcForwardVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11, 1, 2),
    _LecMcForwardVpi_Type()
)
lecMcForwardVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecMcForwardVpi.setStatus("mandatory")
_LecMcForwardVci_Type = VciInteger
_LecMcForwardVci_Object = MibTableColumn
lecMcForwardVci = _LecMcForwardVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11, 1, 3),
    _LecMcForwardVci_Type()
)
lecMcForwardVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecMcForwardVci.setStatus("mandatory")


class _LecMcForwardVerification_Type(Integer32):
    """Custom type lecMcForwardVerification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("implicit", 2),
          ("explicit", 3))
    )


_LecMcForwardVerification_Type.__name__ = "Integer32"
_LecMcForwardVerification_Object = MibTableColumn
lecMcForwardVerification = _LecMcForwardVerification_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 11, 1, 4),
    _LecMcForwardVerification_Type()
)
lecMcForwardVerification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMcForwardVerification.setStatus("mandatory")
_LecQueryObjects_ObjectIdentity = ObjectIdentity
lecQueryObjects = _LecQueryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12)
)
_LecMacQueryObjects_ObjectIdentity = ObjectIdentity
lecMacQueryObjects = _LecMacQueryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1)
)


class _LecMacQueryLecIndex_Type(Integer32):
    """Custom type lecMacQueryLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecMacQueryLecIndex_Type.__name__ = "Integer32"
_LecMacQueryLecIndex_Object = MibScalar
lecMacQueryLecIndex = _LecMacQueryLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 1),
    _LecMacQueryLecIndex_Type()
)
lecMacQueryLecIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMacQueryLecIndex.setStatus("mandatory")
_LecMacQueryAddress_Type = MacAddress
_LecMacQueryAddress_Object = MibScalar
lecMacQueryAddress = _LecMacQueryAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 2),
    _LecMacQueryAddress_Type()
)
lecMacQueryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMacQueryAddress.setStatus("mandatory")


class _LecMacQueryStatus_Type(Integer32):
    """Custom type lecMacQueryStatus based on Integer32"""
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
        *(("none", 1),
          ("unsupported", 2),
          ("local", 3),
          ("remote", 4),
          ("unknown", 5))
    )


_LecMacQueryStatus_Type.__name__ = "Integer32"
_LecMacQueryStatus_Object = MibScalar
lecMacQueryStatus = _LecMacQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 3),
    _LecMacQueryStatus_Type()
)
lecMacQueryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacQueryStatus.setStatus("mandatory")
_LecMacQueryAtmAddress_Type = AtmLaneAddress
_LecMacQueryAtmAddress_Object = MibScalar
lecMacQueryAtmAddress = _LecMacQueryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 4),
    _LecMacQueryAtmAddress_Type()
)
lecMacQueryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacQueryAtmAddress.setStatus("mandatory")
_LecMacQueryMuxedAtmAddress_Type = AtmLaneAddress
_LecMacQueryMuxedAtmAddress_Object = MibScalar
lecMacQueryMuxedAtmAddress = _LecMacQueryMuxedAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 5),
    _LecMacQueryMuxedAtmAddress_Type()
)
lecMacQueryMuxedAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacQueryMuxedAtmAddress.setStatus("mandatory")


class _LecMacQueryServiceCategory_Type(Integer32):
    """Custom type lecMacQueryServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecMacQueryServiceCategory_Type.__name__ = "Integer32"
_LecMacQueryServiceCategory_Object = MibScalar
lecMacQueryServiceCategory = _LecMacQueryServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 1, 6),
    _LecMacQueryServiceCategory_Type()
)
lecMacQueryServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacQueryServiceCategory.setStatus("mandatory")
_LecRDQueryObjects_ObjectIdentity = ObjectIdentity
lecRDQueryObjects = _LecRDQueryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2)
)


class _LecRDQueryLecIndex_Type(Integer32):
    """Custom type lecRDQueryLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecRDQueryLecIndex_Type.__name__ = "Integer32"
_LecRDQueryLecIndex_Object = MibScalar
lecRDQueryLecIndex = _LecRDQueryLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 1),
    _LecRDQueryLecIndex_Type()
)
lecRDQueryLecIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecRDQueryLecIndex.setStatus("mandatory")


class _LecRDQuerySegmentID_Type(Integer32):
    """Custom type lecRDQuerySegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecRDQuerySegmentID_Type.__name__ = "Integer32"
_LecRDQuerySegmentID_Object = MibScalar
lecRDQuerySegmentID = _LecRDQuerySegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 2),
    _LecRDQuerySegmentID_Type()
)
lecRDQuerySegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecRDQuerySegmentID.setStatus("mandatory")


class _LecRDQueryBridgeNumber_Type(Integer32):
    """Custom type lecRDQueryBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LecRDQueryBridgeNumber_Type.__name__ = "Integer32"
_LecRDQueryBridgeNumber_Object = MibScalar
lecRDQueryBridgeNumber = _LecRDQueryBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 3),
    _LecRDQueryBridgeNumber_Type()
)
lecRDQueryBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecRDQueryBridgeNumber.setStatus("mandatory")


class _LecRDQueryStatus_Type(Integer32):
    """Custom type lecRDQueryStatus based on Integer32"""
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
        *(("none", 1),
          ("unsupported", 2),
          ("local", 3),
          ("remote", 4),
          ("unknown", 5))
    )


_LecRDQueryStatus_Type.__name__ = "Integer32"
_LecRDQueryStatus_Object = MibScalar
lecRDQueryStatus = _LecRDQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 4),
    _LecRDQueryStatus_Type()
)
lecRDQueryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRDQueryStatus.setStatus("mandatory")
_LecRDQueryAtmAddress_Type = AtmLaneAddress
_LecRDQueryAtmAddress_Object = MibScalar
lecRDQueryAtmAddress = _LecRDQueryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 5),
    _LecRDQueryAtmAddress_Type()
)
lecRDQueryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRDQueryAtmAddress.setStatus("mandatory")
_LecRDQueryMuxedAtmAddress_Type = AtmLaneAddress
_LecRDQueryMuxedAtmAddress_Object = MibScalar
lecRDQueryMuxedAtmAddress = _LecRDQueryMuxedAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 6),
    _LecRDQueryMuxedAtmAddress_Type()
)
lecRDQueryMuxedAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRDQueryMuxedAtmAddress.setStatus("mandatory")


class _LecRDQueryServiceCategory_Type(Integer32):
    """Custom type lecRDQueryServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LecRDQueryServiceCategory_Type.__name__ = "Integer32"
_LecRDQueryServiceCategory_Object = MibScalar
lecRDQueryServiceCategory = _LecRDQueryServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 12, 2, 7),
    _LecRDQueryServiceCategory_Type()
)
lecRDQueryServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRDQueryServiceCategory.setStatus("mandatory")
_LecTlvTable_Object = MibTable
lecTlvTable = _LecTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    lecTlvTable.setStatus("mandatory")
_LecTlvEntry_Object = MibTableRow
lecTlvEntry = _LecTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1)
)
lecTlvEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecTlvSetIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecTlvLanDestination"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecTlvIndex"),
)
if mibBuilder.loadTexts:
    lecTlvEntry.setStatus("mandatory")


class _LecTlvSetIndex_Type(Integer32):
    """Custom type lecTlvSetIndex based on Integer32"""
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
        *(("layer3Tlvs", 1),
          ("actualRegTlvs", 2),
          ("configRegTlvs", 3),
          ("leArpTlvs", 4),
          ("queryTlvs", 5))
    )


_LecTlvSetIndex_Type.__name__ = "Integer32"
_LecTlvSetIndex_Object = MibTableColumn
lecTlvSetIndex = _LecTlvSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 1),
    _LecTlvSetIndex_Type()
)
lecTlvSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecTlvSetIndex.setStatus("mandatory")


class _LecTlvLanDestination_Type(OctetString):
    """Custom type lecTlvLanDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_LecTlvLanDestination_Type.__name__ = "OctetString"
_LecTlvLanDestination_Object = MibTableColumn
lecTlvLanDestination = _LecTlvLanDestination_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 2),
    _LecTlvLanDestination_Type()
)
lecTlvLanDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecTlvLanDestination.setStatus("mandatory")


class _LecTlvIndex_Type(Integer32):
    """Custom type lecTlvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LecTlvIndex_Type.__name__ = "Integer32"
_LecTlvIndex_Object = MibTableColumn
lecTlvIndex = _LecTlvIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 3),
    _LecTlvIndex_Type()
)
lecTlvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecTlvIndex.setStatus("mandatory")


class _LecTlvType_Type(OctetString):
    """Custom type lecTlvType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_LecTlvType_Type.__name__ = "OctetString"
_LecTlvType_Object = MibTableColumn
lecTlvType = _LecTlvType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 4),
    _LecTlvType_Type()
)
lecTlvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecTlvType.setStatus("mandatory")


class _LecTlvValue_Type(OctetString):
    """Custom type lecTlvValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LecTlvValue_Type.__name__ = "OctetString"
_LecTlvValue_Object = MibTableColumn
lecTlvValue = _LecTlvValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 5),
    _LecTlvValue_Type()
)
lecTlvValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecTlvValue.setStatus("mandatory")
_LecTlvRowStatus_Type = RowStatus
_LecTlvRowStatus_Object = MibTableColumn
lecTlvRowStatus = _LecTlvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 13, 1, 6),
    _LecTlvRowStatus_Type()
)
lecTlvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecTlvRowStatus.setStatus("mandatory")
_LeClientMIBConformance_ObjectIdentity = ObjectIdentity
leClientMIBConformance = _LeClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2)
)
_LeClientMIBGroups_ObjectIdentity = ObjectIdentity
leClientMIBGroups = _LeClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1)
)
_LeClientConfigGroup_ObjectIdentity = ObjectIdentity
leClientConfigGroup = _LeClientConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 1)
)
_LeClientStatusGroup_ObjectIdentity = ObjectIdentity
leClientStatusGroup = _LeClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 2)
)
_LeClientMappingGroup_ObjectIdentity = ObjectIdentity
leClientMappingGroup = _LeClientMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 3)
)
_LeClientStatisticsGroup_ObjectIdentity = ObjectIdentity
leClientStatisticsGroup = _LeClientStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 4)
)
_LeClientServerVccGroup_ObjectIdentity = ObjectIdentity
leClientServerVccGroup = _LeClientServerVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 5)
)
_LeClientAtmAddressesGroup_ObjectIdentity = ObjectIdentity
leClientAtmAddressesGroup = _LeClientAtmAddressesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 6)
)
_LeClientMacAddressesGroup_ObjectIdentity = ObjectIdentity
leClientMacAddressesGroup = _LeClientMacAddressesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 7)
)
_LeClientRouteDescriptorsGroup_ObjectIdentity = ObjectIdentity
leClientRouteDescriptorsGroup = _LeClientRouteDescriptorsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 8)
)
_LeClientArpGroup_ObjectIdentity = ObjectIdentity
leClientArpGroup = _LeClientArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 9)
)
_LeClientRDArpGroup_ObjectIdentity = ObjectIdentity
leClientRDArpGroup = _LeClientRDArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 10)
)
_LeClientMIBCompliances_ObjectIdentity = ObjectIdentity
leClientMIBCompliances = _LeClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 2)
)
_LeClientMIBCompliance_ObjectIdentity = ObjectIdentity
leClientMIBCompliance = _LeClientMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    **{"OwnerString": OwnerString,
       "TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "AtmLaneAddress": AtmLaneAddress,
       "VpiInteger": VpiInteger,
       "VciInteger": VciInteger,
       "LeConnectionInterface": LeConnectionInterface,
       "LecState": LecState,
       "LecDataFrameFormat": LecDataFrameFormat,
       "LecDataFrameSize": LecDataFrameSize,
       "LeArpTableEntryType": LeArpTableEntryType,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfLanEmulation": atmfLanEmulation,
       "leClientMIB": leClientMIB,
       "leClientMIBObjects": leClientMIBObjects,
       "lecConfigTable": lecConfigTable,
       "lecConfigEntry": lecConfigEntry,
       "lecIndex": lecIndex,
       "lecRowStatus": lecRowStatus,
       "lecOwner": lecOwner,
       "lecConfigMode": lecConfigMode,
       "lecConfigLanType": lecConfigLanType,
       "lecConfigMaxDataFrameSize": lecConfigMaxDataFrameSize,
       "lecConfigLanName": lecConfigLanName,
       "lecConfigLesAtmAddress": lecConfigLesAtmAddress,
       "lecControlTimeout": lecControlTimeout,
       "lecMaxUnknownFrameCount": lecMaxUnknownFrameCount,
       "lecMaxUnknownFrameTime": lecMaxUnknownFrameTime,
       "lecVccTimeoutPeriod": lecVccTimeoutPeriod,
       "lecMaxRetryCount": lecMaxRetryCount,
       "lecAgingTime": lecAgingTime,
       "lecForwardDelayTime": lecForwardDelayTime,
       "lecExpectedArpResponseTime": lecExpectedArpResponseTime,
       "lecFlushTimeOut": lecFlushTimeOut,
       "lecPathSwitchingDelay": lecPathSwitchingDelay,
       "lecLocalSegmentID": lecLocalSegmentID,
       "lecMulticastSendType": lecMulticastSendType,
       "lecMulticastSendAvgRate": lecMulticastSendAvgRate,
       "lecMulticastSendPeakRate": lecMulticastSendPeakRate,
       "lecConnectionCompleteTimer": lecConnectionCompleteTimer,
       "lecConfigLecsAtmAddress": lecConfigLecsAtmAddress,
       "lecInitialControlTimeout": lecInitialControlTimeout,
       "lecControlTimeoutMultiplier": lecControlTimeoutMultiplier,
       "lecV2MaxUnknownFrameCount": lecV2MaxUnknownFrameCount,
       "lecConfigLocalSegmentID": lecConfigLocalSegmentID,
       "lecConfigV2Capable": lecConfigV2Capable,
       "lecConfigSelectiveMulticast": lecConfigSelectiveMulticast,
       "lecForwardDisconnectTimeout": lecForwardDisconnectTimeout,
       "lecConfigLLCMultiplexCapable": lecConfigLLCMultiplexCapable,
       "lecMinReconfigureDelay": lecMinReconfigureDelay,
       "lecMaxReconfigureDelay": lecMaxReconfigureDelay,
       "lecMaxBusConnectRetries": lecMaxBusConnectRetries,
       "lecTokenRingExplorerExclude": lecTokenRingExplorerExclude,
       "lecStatusTable": lecStatusTable,
       "lecStatusEntry": lecStatusEntry,
       "lecIfIndex": lecIfIndex,
       "lecPrimaryAtmAddress": lecPrimaryAtmAddress,
       "lecID": lecID,
       "lecInterfaceState": lecInterfaceState,
       "lecLastFailureRespCode": lecLastFailureRespCode,
       "lecLastFailureState": lecLastFailureState,
       "lecProtocol": lecProtocol,
       "lecVersion": lecVersion,
       "lecTopologyChange": lecTopologyChange,
       "lecConfigServerAtmAddress": lecConfigServerAtmAddress,
       "lecConfigSource": lecConfigSource,
       "lecActualLanType": lecActualLanType,
       "lecActualMaxDataFrameSize": lecActualMaxDataFrameSize,
       "lecActualLanName": lecActualLanName,
       "lecActualLesAtmAddress": lecActualLesAtmAddress,
       "lecProxyClient": lecProxyClient,
       "lecActualLocalSegmentID": lecActualLocalSegmentID,
       "lecActualV2Capable": lecActualV2Capable,
       "lecElanID": lecElanID,
       "lecActualSelectiveMulticast": lecActualSelectiveMulticast,
       "lecActualLLCMultiplexCapable": lecActualLLCMultiplexCapable,
       "lecPreferredLesAddress": lecPreferredLesAddress,
       "lecStoresServiceCategories": lecStoresServiceCategories,
       "lecMappingTable": lecMappingTable,
       "lecMappingEntry": lecMappingEntry,
       "lecMappingIndex": lecMappingIndex,
       "lecStatisticsTable": lecStatisticsTable,
       "lecStatisticsEntry": lecStatisticsEntry,
       "lecArpRequestsOut": lecArpRequestsOut,
       "lecArpRequestsIn": lecArpRequestsIn,
       "lecArpRepliesOut": lecArpRepliesOut,
       "lecArpRepliesIn": lecArpRepliesIn,
       "lecControlFramesOut": lecControlFramesOut,
       "lecControlFramesIn": lecControlFramesIn,
       "lecSvcFailures": lecSvcFailures,
       "lecFlowFailures": lecFlowFailures,
       "lecEchoDiscards": lecEchoDiscards,
       "lecFilteredMulticasts": lecFilteredMulticasts,
       "lecServerVccTable": lecServerVccTable,
       "lecServerVccEntry": lecServerVccEntry,
       "lecConfigDirectInterface": lecConfigDirectInterface,
       "lecConfigDirectVpi": lecConfigDirectVpi,
       "lecConfigDirectVci": lecConfigDirectVci,
       "lecControlDirectInterface": lecControlDirectInterface,
       "lecControlDirectVpi": lecControlDirectVpi,
       "lecControlDirectVci": lecControlDirectVci,
       "lecControlDistributeInterface": lecControlDistributeInterface,
       "lecControlDistributeVpi": lecControlDistributeVpi,
       "lecControlDistributeVci": lecControlDistributeVci,
       "lecMulticastSendInterface": lecMulticastSendInterface,
       "lecMulticastSendVpi": lecMulticastSendVpi,
       "lecMulticastSendVci": lecMulticastSendVci,
       "lecMulticastForwardInterface": lecMulticastForwardInterface,
       "lecMulticastForwardVpi": lecMulticastForwardVpi,
       "lecMulticastForwardVci": lecMulticastForwardVci,
       "lecAtmAddressTable": lecAtmAddressTable,
       "lecAtmAddressEntry": lecAtmAddressEntry,
       "lecAtmAddress": lecAtmAddress,
       "lecAtmAddressStatus": lecAtmAddressStatus,
       "lecAtmAddressMuxed": lecAtmAddressMuxed,
       "lecMacAddressTable": lecMacAddressTable,
       "lecMacAddressEntry": lecMacAddressEntry,
       "lecMacAddress": lecMacAddress,
       "lecMacAddressAtmBinding": lecMacAddressAtmBinding,
       "lecMacAddressMuxedAtmBinding": lecMacAddressMuxedAtmBinding,
       "lecMacAddressServiceCategory": lecMacAddressServiceCategory,
       "lecRouteDescrTable": lecRouteDescrTable,
       "lecRouteDescrEntry": lecRouteDescrEntry,
       "lecRouteDescrSegmentID": lecRouteDescrSegmentID,
       "lecRouteDescrBridgeNumber": lecRouteDescrBridgeNumber,
       "lecRouteDescrAtmBinding": lecRouteDescrAtmBinding,
       "lecRouteDescrMuxedAtmBinding": lecRouteDescrMuxedAtmBinding,
       "lecRouteDescrServiceCategory": lecRouteDescrServiceCategory,
       "leArpTable": leArpTable,
       "leArpEntry": leArpEntry,
       "leArpMacAddress": leArpMacAddress,
       "leArpAtmAddress": leArpAtmAddress,
       "leArpIsRemoteAddress": leArpIsRemoteAddress,
       "leArpEntryType": leArpEntryType,
       "leArpRowStatus": leArpRowStatus,
       "leArpMuxedAtmAddress": leArpMuxedAtmAddress,
       "leArpServiceCategory": leArpServiceCategory,
       "leRDArpTable": leRDArpTable,
       "leRDArpEntry": leRDArpEntry,
       "leRDArpSegmentID": leRDArpSegmentID,
       "leRDArpBridgeNumber": leRDArpBridgeNumber,
       "leRDArpAtmAddress": leRDArpAtmAddress,
       "leRDArpEntryType": leRDArpEntryType,
       "leRDArpRowStatus": leRDArpRowStatus,
       "leRDArpMuxedAtmAddress": leRDArpMuxedAtmAddress,
       "leRDArpServiceCategory": leRDArpServiceCategory,
       "leRDArpIsRemoteDescriptor": leRDArpIsRemoteDescriptor,
       "lecMcForwardTable": lecMcForwardTable,
       "lecMcForwardEntry": lecMcForwardEntry,
       "lecMcForwardInterface": lecMcForwardInterface,
       "lecMcForwardVpi": lecMcForwardVpi,
       "lecMcForwardVci": lecMcForwardVci,
       "lecMcForwardVerification": lecMcForwardVerification,
       "lecQueryObjects": lecQueryObjects,
       "lecMacQueryObjects": lecMacQueryObjects,
       "lecMacQueryLecIndex": lecMacQueryLecIndex,
       "lecMacQueryAddress": lecMacQueryAddress,
       "lecMacQueryStatus": lecMacQueryStatus,
       "lecMacQueryAtmAddress": lecMacQueryAtmAddress,
       "lecMacQueryMuxedAtmAddress": lecMacQueryMuxedAtmAddress,
       "lecMacQueryServiceCategory": lecMacQueryServiceCategory,
       "lecRDQueryObjects": lecRDQueryObjects,
       "lecRDQueryLecIndex": lecRDQueryLecIndex,
       "lecRDQuerySegmentID": lecRDQuerySegmentID,
       "lecRDQueryBridgeNumber": lecRDQueryBridgeNumber,
       "lecRDQueryStatus": lecRDQueryStatus,
       "lecRDQueryAtmAddress": lecRDQueryAtmAddress,
       "lecRDQueryMuxedAtmAddress": lecRDQueryMuxedAtmAddress,
       "lecRDQueryServiceCategory": lecRDQueryServiceCategory,
       "lecTlvTable": lecTlvTable,
       "lecTlvEntry": lecTlvEntry,
       "lecTlvSetIndex": lecTlvSetIndex,
       "lecTlvLanDestination": lecTlvLanDestination,
       "lecTlvIndex": lecTlvIndex,
       "lecTlvType": lecTlvType,
       "lecTlvValue": lecTlvValue,
       "lecTlvRowStatus": lecTlvRowStatus,
       "leClientMIBConformance": leClientMIBConformance,
       "leClientMIBGroups": leClientMIBGroups,
       "leClientConfigGroup": leClientConfigGroup,
       "leClientStatusGroup": leClientStatusGroup,
       "leClientMappingGroup": leClientMappingGroup,
       "leClientStatisticsGroup": leClientStatisticsGroup,
       "leClientServerVccGroup": leClientServerVccGroup,
       "leClientAtmAddressesGroup": leClientAtmAddressesGroup,
       "leClientMacAddressesGroup": leClientMacAddressesGroup,
       "leClientRouteDescriptorsGroup": leClientRouteDescriptorsGroup,
       "leClientArpGroup": leClientArpGroup,
       "leClientRDArpGroup": leClientRDArpGroup,
       "leClientMIBCompliances": leClientMIBCompliances,
       "leClientMIBCompliance": leClientMIBCompliance}
)
