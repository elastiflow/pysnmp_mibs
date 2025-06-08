# SNMP MIB module (SCTE-HMS-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-VOIP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:36:31 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(voipIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "voipIdent")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

voipModuleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Rfactor(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
        ValueRangeConstraint(127, 127),
    )



class ScaledMOSscore(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
        ValueRangeConstraint(127, 127),
    )



# MIB Managed Objects in the order of their OIDs

_VoipMibObjects_ObjectIdentity = ObjectIdentity
voipMibObjects = _VoipMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1)
)


class _VoipVersion_Type(SnmpAdminString):
    """Custom type voipVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipVersion_Type.__name__ = "SnmpAdminString"
_VoipVersion_Object = MibScalar
voipVersion = _VoipVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 1),
    _VoipVersion_Type()
)
voipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipVersion.setStatus("current")
_VoipMaxTestInstance_Type = Unsigned32
_VoipMaxTestInstance_Object = MibScalar
voipMaxTestInstance = _VoipMaxTestInstance_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 2),
    _VoipMaxTestInstance_Type()
)
voipMaxTestInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipMaxTestInstance.setStatus("current")
_VoipTest_ObjectIdentity = ObjectIdentity
voipTest = _VoipTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3)
)
_VoipTestControlTable_Object = MibTable
voipTestControlTable = _VoipTestControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    voipTestControlTable.setStatus("current")
_VoipTestControlEntry_Object = MibTableRow
voipTestControlEntry = _VoipTestControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1)
)
voipTestControlEntry.setIndexNames(
    (0, "SCTE-HMS-VOIP-MIB", "voipTestControlIndex"),
)
if mibBuilder.loadTexts:
    voipTestControlEntry.setStatus("current")
_VoipTestControlIndex_Type = Unsigned32
_VoipTestControlIndex_Object = MibTableColumn
voipTestControlIndex = _VoipTestControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 1),
    _VoipTestControlIndex_Type()
)
voipTestControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipTestControlIndex.setStatus("current")


class _VoipTestControlIdString_Type(SnmpAdminString):
    """Custom type voipTestControlIdString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipTestControlIdString_Type.__name__ = "SnmpAdminString"
_VoipTestControlIdString_Object = MibTableColumn
voipTestControlIdString = _VoipTestControlIdString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 2),
    _VoipTestControlIdString_Type()
)
voipTestControlIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestControlIdString.setStatus("current")


class _VoipTestControl_Type(Integer32):
    """Custom type voipTestControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopTest", 1),
          ("setupTest", 2),
          ("startTest", 3))
    )


_VoipTestControl_Type.__name__ = "Integer32"
_VoipTestControl_Object = MibTableColumn
voipTestControl = _VoipTestControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 3),
    _VoipTestControl_Type()
)
voipTestControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestControl.setStatus("current")
_VoipTestSenderAddressType_Type = InetAddressType
_VoipTestSenderAddressType_Object = MibTableColumn
voipTestSenderAddressType = _VoipTestSenderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 4),
    _VoipTestSenderAddressType_Type()
)
voipTestSenderAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestSenderAddressType.setStatus("current")
_VoipTestSenderAddress_Type = InetAddress
_VoipTestSenderAddress_Object = MibTableColumn
voipTestSenderAddress = _VoipTestSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 5),
    _VoipTestSenderAddress_Type()
)
voipTestSenderAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestSenderAddress.setStatus("current")
_VoipTestSenderUDPPort_Type = InetPortNumber
_VoipTestSenderUDPPort_Object = MibTableColumn
voipTestSenderUDPPort = _VoipTestSenderUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 6),
    _VoipTestSenderUDPPort_Type()
)
voipTestSenderUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestSenderUDPPort.setStatus("current")
_VoipTestReceiverAddressType_Type = InetAddressType
_VoipTestReceiverAddressType_Object = MibTableColumn
voipTestReceiverAddressType = _VoipTestReceiverAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 7),
    _VoipTestReceiverAddressType_Type()
)
voipTestReceiverAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestReceiverAddressType.setStatus("current")
_VoipTestReceiverAddress_Type = InetAddress
_VoipTestReceiverAddress_Object = MibTableColumn
voipTestReceiverAddress = _VoipTestReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 8),
    _VoipTestReceiverAddress_Type()
)
voipTestReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestReceiverAddress.setStatus("current")
_VoipTestReceiverUDPPort_Type = InetPortNumber
_VoipTestReceiverUDPPort_Object = MibTableColumn
voipTestReceiverUDPPort = _VoipTestReceiverUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 9),
    _VoipTestReceiverUDPPort_Type()
)
voipTestReceiverUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestReceiverUDPPort.setStatus("current")


class _VoipTestPacketInterval_Type(Unsigned32):
    """Custom type voipTestPacketInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
    )


_VoipTestPacketInterval_Type.__name__ = "Unsigned32"
_VoipTestPacketInterval_Object = MibTableColumn
voipTestPacketInterval = _VoipTestPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 10),
    _VoipTestPacketInterval_Type()
)
voipTestPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestPacketInterval.setStatus("current")
if mibBuilder.loadTexts:
    voipTestPacketInterval.setUnits("milliseconds")


class _VoipTestNumOfPackets_Type(Unsigned32):
    """Custom type voipTestNumOfPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_VoipTestNumOfPackets_Type.__name__ = "Unsigned32"
_VoipTestNumOfPackets_Object = MibTableColumn
voipTestNumOfPackets = _VoipTestNumOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 11),
    _VoipTestNumOfPackets_Type()
)
voipTestNumOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestNumOfPackets.setStatus("current")


class _VoipTestJitterBufferSize_Type(Unsigned32):
    """Custom type voipTestJitterBufferSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_VoipTestJitterBufferSize_Type.__name__ = "Unsigned32"
_VoipTestJitterBufferSize_Object = MibTableColumn
voipTestJitterBufferSize = _VoipTestJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 12),
    _VoipTestJitterBufferSize_Type()
)
voipTestJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestJitterBufferSize.setStatus("current")


class _VoipTestCodecType_Type(OctetString):
    """Custom type voipTestCodecType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VoipTestCodecType_Type.__name__ = "OctetString"
_VoipTestCodecType_Object = MibTableColumn
voipTestCodecType = _VoipTestCodecType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 13),
    _VoipTestCodecType_Type()
)
voipTestCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestCodecType.setStatus("current")


class _VoipTestRoundTripTimeEstimate_Type(Unsigned32):
    """Custom type voipTestRoundTripTimeEstimate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VoipTestRoundTripTimeEstimate_Type.__name__ = "Unsigned32"
_VoipTestRoundTripTimeEstimate_Object = MibTableColumn
voipTestRoundTripTimeEstimate = _VoipTestRoundTripTimeEstimate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 1, 1, 14),
    _VoipTestRoundTripTimeEstimate_Type()
)
voipTestRoundTripTimeEstimate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipTestRoundTripTimeEstimate.setStatus("current")
if mibBuilder.loadTexts:
    voipTestRoundTripTimeEstimate.setUnits("milliseconds")
_VoipTestResultTable_Object = MibTable
voipTestResultTable = _VoipTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    voipTestResultTable.setStatus("current")
_VoipTestResultEntry_Object = MibTableRow
voipTestResultEntry = _VoipTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1)
)
voipTestResultEntry.setIndexNames(
    (0, "SCTE-HMS-VOIP-MIB", "voipTestResultIndex"),
)
if mibBuilder.loadTexts:
    voipTestResultEntry.setStatus("current")
_VoipTestResultIndex_Type = Unsigned32
_VoipTestResultIndex_Object = MibTableColumn
voipTestResultIndex = _VoipTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 1),
    _VoipTestResultIndex_Type()
)
voipTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipTestResultIndex.setStatus("current")


class _VoipTestResultIdString_Type(SnmpAdminString):
    """Custom type voipTestResultIdString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipTestResultIdString_Type.__name__ = "SnmpAdminString"
_VoipTestResultIdString_Object = MibTableColumn
voipTestResultIdString = _VoipTestResultIdString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 2),
    _VoipTestResultIdString_Type()
)
voipTestResultIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestResultIdString.setStatus("current")


class _VoipTestStatus_Type(Integer32):
    """Custom type voipTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("running", 1),
          ("completed", 2),
          ("resourceUnavailable", 3),
          ("invalidParameter", 4),
          ("ready", 5),
          ("other", 6))
    )


_VoipTestStatus_Type.__name__ = "Integer32"
_VoipTestStatus_Object = MibTableColumn
voipTestStatus = _VoipTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 3),
    _VoipTestStatus_Type()
)
voipTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestStatus.setStatus("current")


class _VoipTestStatusString_Type(SnmpAdminString):
    """Custom type voipTestStatusString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipTestStatusString_Type.__name__ = "SnmpAdminString"
_VoipTestStatusString_Object = MibTableColumn
voipTestStatusString = _VoipTestStatusString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 4),
    _VoipTestStatusString_Type()
)
voipTestStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestStatusString.setStatus("current")
_VoipTestDuration_Type = Unsigned32
_VoipTestDuration_Object = MibTableColumn
voipTestDuration = _VoipTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 5),
    _VoipTestDuration_Type()
)
voipTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    voipTestDuration.setUnits("milliseconds")
_VoipTestStartTime_Type = DateAndTime
_VoipTestStartTime_Object = MibTableColumn
voipTestStartTime = _VoipTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 6),
    _VoipTestStartTime_Type()
)
voipTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestStartTime.setStatus("current")
_VoipTestStopTime_Type = DateAndTime
_VoipTestStopTime_Object = MibTableColumn
voipTestStopTime = _VoipTestStopTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 7),
    _VoipTestStopTime_Type()
)
voipTestStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestStopTime.setStatus("current")
_VoipTestProcessedPacketCount_Type = Counter32
_VoipTestProcessedPacketCount_Object = MibTableColumn
voipTestProcessedPacketCount = _VoipTestProcessedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 8),
    _VoipTestProcessedPacketCount_Type()
)
voipTestProcessedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestProcessedPacketCount.setStatus("current")
_VoipTestLossPacketCount_Type = Counter32
_VoipTestLossPacketCount_Object = MibTableColumn
voipTestLossPacketCount = _VoipTestLossPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 9),
    _VoipTestLossPacketCount_Type()
)
voipTestLossPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestLossPacketCount.setStatus("current")
_VoipTestDiscardedPacketCount_Type = Counter32
_VoipTestDiscardedPacketCount_Object = MibTableColumn
voipTestDiscardedPacketCount = _VoipTestDiscardedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 10),
    _VoipTestDiscardedPacketCount_Type()
)
voipTestDiscardedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestDiscardedPacketCount.setStatus("current")
_VoipTestMinJitterLevel_Type = Counter32
_VoipTestMinJitterLevel_Object = MibTableColumn
voipTestMinJitterLevel = _VoipTestMinJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 11),
    _VoipTestMinJitterLevel_Type()
)
voipTestMinJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestMinJitterLevel.setStatus("current")
_VoipTestMaxJitterLevel_Type = Counter32
_VoipTestMaxJitterLevel_Object = MibTableColumn
voipTestMaxJitterLevel = _VoipTestMaxJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 12),
    _VoipTestMaxJitterLevel_Type()
)
voipTestMaxJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestMaxJitterLevel.setStatus("current")
_VoipTestAvgJitterLevel_Type = Counter32
_VoipTestAvgJitterLevel_Object = MibTableColumn
voipTestAvgJitterLevel = _VoipTestAvgJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 13),
    _VoipTestAvgJitterLevel_Type()
)
voipTestAvgJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestAvgJitterLevel.setStatus("current")
_VoipTestRfactor_Type = Rfactor
_VoipTestRfactor_Object = MibTableColumn
voipTestRfactor = _VoipTestRfactor_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 14),
    _VoipTestRfactor_Type()
)
voipTestRfactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestRfactor.setStatus("current")
_VoipTestMOS_Type = ScaledMOSscore
_VoipTestMOS_Object = MibTableColumn
voipTestMOS = _VoipTestMOS_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 1, 3, 2, 1, 15),
    _VoipTestMOS_Type()
)
voipTestMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipTestMOS.setStatus("current")
_VoipMibConformance_ObjectIdentity = ObjectIdentity
voipMibConformance = _VoipMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2)
)
_VoipMibCompliances_ObjectIdentity = ObjectIdentity
voipMibCompliances = _VoipMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 1)
)
_VoipMibGroups_ObjectIdentity = ObjectIdentity
voipMibGroups = _VoipMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 2)
)

# Managed Objects groups

voipMibObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 2, 1)
)
voipMibObjectsGroup.setObjects(
      *(("SCTE-HMS-VOIP-MIB", "voipVersion"),
        ("SCTE-HMS-VOIP-MIB", "voipMaxTestInstance"))
)
if mibBuilder.loadTexts:
    voipMibObjectsGroup.setStatus("current")

voipTestControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 2, 2)
)
voipTestControlGroup.setObjects(
      *(("SCTE-HMS-VOIP-MIB", "voipTestControlIdString"),
        ("SCTE-HMS-VOIP-MIB", "voipTestControl"),
        ("SCTE-HMS-VOIP-MIB", "voipTestSenderAddressType"),
        ("SCTE-HMS-VOIP-MIB", "voipTestSenderAddress"),
        ("SCTE-HMS-VOIP-MIB", "voipTestSenderUDPPort"),
        ("SCTE-HMS-VOIP-MIB", "voipTestReceiverAddressType"),
        ("SCTE-HMS-VOIP-MIB", "voipTestReceiverAddress"),
        ("SCTE-HMS-VOIP-MIB", "voipTestReceiverUDPPort"),
        ("SCTE-HMS-VOIP-MIB", "voipTestPacketInterval"),
        ("SCTE-HMS-VOIP-MIB", "voipTestNumOfPackets"),
        ("SCTE-HMS-VOIP-MIB", "voipTestJitterBufferSize"),
        ("SCTE-HMS-VOIP-MIB", "voipTestCodecType"),
        ("SCTE-HMS-VOIP-MIB", "voipTestRoundTripTimeEstimate"))
)
if mibBuilder.loadTexts:
    voipTestControlGroup.setStatus("current")

voipTestResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 2, 3)
)
voipTestResultGroup.setObjects(
      *(("SCTE-HMS-VOIP-MIB", "voipTestResultIdString"),
        ("SCTE-HMS-VOIP-MIB", "voipTestStatus"),
        ("SCTE-HMS-VOIP-MIB", "voipTestStatusString"),
        ("SCTE-HMS-VOIP-MIB", "voipTestDuration"),
        ("SCTE-HMS-VOIP-MIB", "voipTestStartTime"),
        ("SCTE-HMS-VOIP-MIB", "voipTestStopTime"),
        ("SCTE-HMS-VOIP-MIB", "voipTestProcessedPacketCount"),
        ("SCTE-HMS-VOIP-MIB", "voipTestLossPacketCount"),
        ("SCTE-HMS-VOIP-MIB", "voipTestDiscardedPacketCount"),
        ("SCTE-HMS-VOIP-MIB", "voipTestMinJitterLevel"),
        ("SCTE-HMS-VOIP-MIB", "voipTestMaxJitterLevel"),
        ("SCTE-HMS-VOIP-MIB", "voipTestAvgJitterLevel"),
        ("SCTE-HMS-VOIP-MIB", "voipTestRfactor"),
        ("SCTE-HMS-VOIP-MIB", "voipTestMOS"))
)
if mibBuilder.loadTexts:
    voipTestResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

voipCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12, 1, 1, 2, 1, 1)
)
voipCompliances.setObjects(
      *(("SCTE-HMS-VOIP-MIB", "voipMibObjectsGroup"),
        ("SCTE-HMS-VOIP-MIB", "voipTestControlGroup"),
        ("SCTE-HMS-VOIP-MIB", "voipTestResultGroup"))
)
if mibBuilder.loadTexts:
    voipCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-VOIP-MIB",
    **{"Rfactor": Rfactor,
       "ScaledMOSscore": ScaledMOSscore,
       "voipModuleMib": voipModuleMib,
       "voipMibObjects": voipMibObjects,
       "voipVersion": voipVersion,
       "voipMaxTestInstance": voipMaxTestInstance,
       "voipTest": voipTest,
       "voipTestControlTable": voipTestControlTable,
       "voipTestControlEntry": voipTestControlEntry,
       "voipTestControlIndex": voipTestControlIndex,
       "voipTestControlIdString": voipTestControlIdString,
       "voipTestControl": voipTestControl,
       "voipTestSenderAddressType": voipTestSenderAddressType,
       "voipTestSenderAddress": voipTestSenderAddress,
       "voipTestSenderUDPPort": voipTestSenderUDPPort,
       "voipTestReceiverAddressType": voipTestReceiverAddressType,
       "voipTestReceiverAddress": voipTestReceiverAddress,
       "voipTestReceiverUDPPort": voipTestReceiverUDPPort,
       "voipTestPacketInterval": voipTestPacketInterval,
       "voipTestNumOfPackets": voipTestNumOfPackets,
       "voipTestJitterBufferSize": voipTestJitterBufferSize,
       "voipTestCodecType": voipTestCodecType,
       "voipTestRoundTripTimeEstimate": voipTestRoundTripTimeEstimate,
       "voipTestResultTable": voipTestResultTable,
       "voipTestResultEntry": voipTestResultEntry,
       "voipTestResultIndex": voipTestResultIndex,
       "voipTestResultIdString": voipTestResultIdString,
       "voipTestStatus": voipTestStatus,
       "voipTestStatusString": voipTestStatusString,
       "voipTestDuration": voipTestDuration,
       "voipTestStartTime": voipTestStartTime,
       "voipTestStopTime": voipTestStopTime,
       "voipTestProcessedPacketCount": voipTestProcessedPacketCount,
       "voipTestLossPacketCount": voipTestLossPacketCount,
       "voipTestDiscardedPacketCount": voipTestDiscardedPacketCount,
       "voipTestMinJitterLevel": voipTestMinJitterLevel,
       "voipTestMaxJitterLevel": voipTestMaxJitterLevel,
       "voipTestAvgJitterLevel": voipTestAvgJitterLevel,
       "voipTestRfactor": voipTestRfactor,
       "voipTestMOS": voipTestMOS,
       "voipMibConformance": voipMibConformance,
       "voipMibCompliances": voipMibCompliances,
       "voipCompliances": voipCompliances,
       "voipMibGroups": voipMibGroups,
       "voipMibObjectsGroup": voipMibObjectsGroup,
       "voipTestControlGroup": voipTestControlGroup,
       "voipTestResultGroup": voipTestResultGroup}
)
