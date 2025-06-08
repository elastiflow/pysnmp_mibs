# SNMP MIB module (A3COM-HUAWEI-VOCALLHISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-VOCALLHISTORY-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:00:40 2025
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

(CodecType,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-VO-TYPE-MIB",
    "CodecType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

h3cVoiceCallHistory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7)
)
if mibBuilder.loadTexts:
    h3cVoiceCallHistory.setRevisions(
        ("2005-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoCallHistoryObjects_ObjectIdentity = ObjectIdentity
h3cVoCallHistoryObjects = _H3cVoCallHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1)
)
_H3cVoCallHistoryMaxLen_Type = Integer32
_H3cVoCallHistoryMaxLen_Object = MibScalar
h3cVoCallHistoryMaxLen = _H3cVoCallHistoryMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1, 1),
    _H3cVoCallHistoryMaxLen_Type()
)
h3cVoCallHistoryMaxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoCallHistoryMaxLen.setStatus("current")


class _H3cVoCallHistoryMaxRetainTime_Type(Integer32):
    """Custom type h3cVoCallHistoryMaxRetainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoCallHistoryMaxRetainTime_Type.__name__ = "Integer32"
_H3cVoCallHistoryMaxRetainTime_Object = MibScalar
h3cVoCallHistoryMaxRetainTime = _H3cVoCallHistoryMaxRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1, 2),
    _H3cVoCallHistoryMaxRetainTime_Type()
)
h3cVoCallHistoryMaxRetainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoCallHistoryMaxRetainTime.setStatus("current")
_H3cVoCallHistoryGenericTable_Object = MibTable
h3cVoCallHistoryGenericTable = _H3cVoCallHistoryGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2)
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryGenericTable.setStatus("current")
_H3cVoCallHistoryGenericEntry_Object = MibTableRow
h3cVoCallHistoryGenericEntry = _H3cVoCallHistoryGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1)
)
h3cVoCallHistoryGenericEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisIndex"),
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryGenericEntry.setStatus("current")


class _H3cVoCallHisIndex_Type(Integer32):
    """Custom type h3cVoCallHisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoCallHisIndex_Type.__name__ = "Integer32"
_H3cVoCallHisIndex_Object = MibTableColumn
h3cVoCallHisIndex = _H3cVoCallHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 1),
    _H3cVoCallHisIndex_Type()
)
h3cVoCallHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoCallHisIndex.setStatus("current")
_H3cVoCallHisCallerNumber_Type = OctetString
_H3cVoCallHisCallerNumber_Object = MibTableColumn
h3cVoCallHisCallerNumber = _H3cVoCallHisCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 2),
    _H3cVoCallHisCallerNumber_Type()
)
h3cVoCallHisCallerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisCallerNumber.setStatus("current")
_H3cVoCallHisCalledNumber_Type = OctetString
_H3cVoCallHisCalledNumber_Object = MibTableColumn
h3cVoCallHisCalledNumber = _H3cVoCallHisCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 3),
    _H3cVoCallHisCalledNumber_Type()
)
h3cVoCallHisCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisCalledNumber.setStatus("current")
_H3cVoCallHisEncodeType_Type = CodecType
_H3cVoCallHisEncodeType_Object = MibTableColumn
h3cVoCallHisEncodeType = _H3cVoCallHisEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 4),
    _H3cVoCallHisEncodeType_Type()
)
h3cVoCallHisEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisEncodeType.setStatus("current")
_H3cVoCallHisChannel_Type = Integer32
_H3cVoCallHisChannel_Object = MibTableColumn
h3cVoCallHisChannel = _H3cVoCallHisChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 5),
    _H3cVoCallHisChannel_Type()
)
h3cVoCallHisChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisChannel.setStatus("current")
_H3cVoCallHisLocalAddressType_Type = InetAddressType
_H3cVoCallHisLocalAddressType_Object = MibTableColumn
h3cVoCallHisLocalAddressType = _H3cVoCallHisLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 6),
    _H3cVoCallHisLocalAddressType_Type()
)
h3cVoCallHisLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisLocalAddressType.setStatus("current")
_H3cVoCallHisLocalAddress_Type = InetAddress
_H3cVoCallHisLocalAddress_Object = MibTableColumn
h3cVoCallHisLocalAddress = _H3cVoCallHisLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 7),
    _H3cVoCallHisLocalAddress_Type()
)
h3cVoCallHisLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisLocalAddress.setStatus("current")
_H3cVoCallHisPeerAddressType_Type = InetAddressType
_H3cVoCallHisPeerAddressType_Object = MibTableColumn
h3cVoCallHisPeerAddressType = _H3cVoCallHisPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 8),
    _H3cVoCallHisPeerAddressType_Type()
)
h3cVoCallHisPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPeerAddressType.setStatus("current")
_H3cVoCallHisPeerAddress_Type = InetAddress
_H3cVoCallHisPeerAddress_Object = MibTableColumn
h3cVoCallHisPeerAddress = _H3cVoCallHisPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 9),
    _H3cVoCallHisPeerAddress_Type()
)
h3cVoCallHisPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPeerAddress.setStatus("current")


class _H3cVoCallHisDisconnectText_Type(Integer32):
    """Custom type h3cVoCallHisDisconnectText based on Integer32"""
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
        *(("normalRelease", 1),
          ("cardNumberNotExist", 2),
          ("invalidPassword", 3),
          ("thisAccountsIsUsing", 4),
          ("noEnoughBalance", 5),
          ("theAccountsIsExpired", 6),
          ("creditLimit", 7),
          ("userReject", 8),
          ("serviceInvalid", 9),
          ("calledLimit", 10),
          ("maxRedialTimesLimit", 11),
          ("invalidParameter", 12),
          ("callerHookOn", 13),
          ("calledHookOn", 14),
          ("networkProblem", 15),
          ("unknownReason", 16))
    )


_H3cVoCallHisDisconnectText_Type.__name__ = "Integer32"
_H3cVoCallHisDisconnectText_Object = MibTableColumn
h3cVoCallHisDisconnectText = _H3cVoCallHisDisconnectText_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 10),
    _H3cVoCallHisDisconnectText_Type()
)
h3cVoCallHisDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisDisconnectText.setStatus("current")
_H3cVoCallHisCallDuration_Type = TimeTicks
_H3cVoCallHisCallDuration_Object = MibTableColumn
h3cVoCallHisCallDuration = _H3cVoCallHisCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 11),
    _H3cVoCallHisCallDuration_Type()
)
h3cVoCallHisCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisCallDuration.setStatus("current")
_H3cVoCallHisVoCallDuration_Type = TimeTicks
_H3cVoCallHisVoCallDuration_Object = MibTableColumn
h3cVoCallHisVoCallDuration = _H3cVoCallHisVoCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 12),
    _H3cVoCallHisVoCallDuration_Type()
)
h3cVoCallHisVoCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoCallDuration.setStatus("current")
_H3cVoCallHisFaxCallDuration_Type = TimeTicks
_H3cVoCallHisFaxCallDuration_Object = MibTableColumn
h3cVoCallHisFaxCallDuration = _H3cVoCallHisFaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 13),
    _H3cVoCallHisFaxCallDuration_Type()
)
h3cVoCallHisFaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisFaxCallDuration.setStatus("current")
_H3cVoCallHisImgPages_Type = Integer32
_H3cVoCallHisImgPages_Object = MibTableColumn
h3cVoCallHisImgPages = _H3cVoCallHisImgPages_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 14),
    _H3cVoCallHisImgPages_Type()
)
h3cVoCallHisImgPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisImgPages.setStatus("current")


class _H3cVoCallHisCallOrigin_Type(Integer32):
    """Custom type h3cVoCallHisCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caller", 1),
          ("called", 2))
    )


_H3cVoCallHisCallOrigin_Type.__name__ = "Integer32"
_H3cVoCallHisCallOrigin_Object = MibTableColumn
h3cVoCallHisCallOrigin = _H3cVoCallHisCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 15),
    _H3cVoCallHisCallOrigin_Type()
)
h3cVoCallHisCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisCallOrigin.setStatus("current")
_H3cVoCallHistoryVoIPTable_Object = MibTable
h3cVoCallHistoryVoIPTable = _H3cVoCallHistoryVoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3)
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryVoIPTable.setStatus("current")
_H3cVoCallHistoryVoIPEntry_Object = MibTableRow
h3cVoCallHistoryVoIPEntry = _H3cVoCallHistoryVoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1)
)
h3cVoCallHistoryVoIPEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisVoIPIndex"),
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryVoIPEntry.setStatus("current")


class _H3cVoCallHisVoIPIndex_Type(Integer32):
    """Custom type h3cVoCallHisVoIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoCallHisVoIPIndex_Type.__name__ = "Integer32"
_H3cVoCallHisVoIPIndex_Object = MibTableColumn
h3cVoCallHisVoIPIndex = _H3cVoCallHisVoIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 1),
    _H3cVoCallHisVoIPIndex_Type()
)
h3cVoCallHisVoIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPIndex.setStatus("current")
_H3cVoCallHisVoIPSetupTime_Type = DateAndTime
_H3cVoCallHisVoIPSetupTime_Object = MibTableColumn
h3cVoCallHisVoIPSetupTime = _H3cVoCallHisVoIPSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 2),
    _H3cVoCallHisVoIPSetupTime_Type()
)
h3cVoCallHisVoIPSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPSetupTime.setStatus("current")
_H3cVoCallHisVoIPConnTime_Type = DateAndTime
_H3cVoCallHisVoIPConnTime_Object = MibTableColumn
h3cVoCallHisVoIPConnTime = _H3cVoCallHisVoIPConnTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 3),
    _H3cVoCallHisVoIPConnTime_Type()
)
h3cVoCallHisVoIPConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPConnTime.setStatus("current")
_H3cVoCallHisVoIPDiscTime_Type = DateAndTime
_H3cVoCallHisVoIPDiscTime_Object = MibTableColumn
h3cVoCallHisVoIPDiscTime = _H3cVoCallHisVoIPDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 4),
    _H3cVoCallHisVoIPDiscTime_Type()
)
h3cVoCallHisVoIPDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPDiscTime.setStatus("current")
_H3cVoCallHisVoIPTxPackets_Type = Counter32
_H3cVoCallHisVoIPTxPackets_Object = MibTableColumn
h3cVoCallHisVoIPTxPackets = _H3cVoCallHisVoIPTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 5),
    _H3cVoCallHisVoIPTxPackets_Type()
)
h3cVoCallHisVoIPTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPTxPackets.setStatus("current")
_H3cVoCallHisVoIPTxBytes_Type = Counter32
_H3cVoCallHisVoIPTxBytes_Object = MibTableColumn
h3cVoCallHisVoIPTxBytes = _H3cVoCallHisVoIPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 6),
    _H3cVoCallHisVoIPTxBytes_Type()
)
h3cVoCallHisVoIPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPTxBytes.setStatus("current")
_H3cVoCallHisVoIPRxPackets_Type = Counter32
_H3cVoCallHisVoIPRxPackets_Object = MibTableColumn
h3cVoCallHisVoIPRxPackets = _H3cVoCallHisVoIPRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 7),
    _H3cVoCallHisVoIPRxPackets_Type()
)
h3cVoCallHisVoIPRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPRxPackets.setStatus("current")
_H3cVoCallHisVoIPRxeBytes_Type = Counter32
_H3cVoCallHisVoIPRxeBytes_Object = MibTableColumn
h3cVoCallHisVoIPRxeBytes = _H3cVoCallHisVoIPRxeBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 8),
    _H3cVoCallHisVoIPRxeBytes_Type()
)
h3cVoCallHisVoIPRxeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisVoIPRxeBytes.setStatus("current")
_H3cVoCallHistoryPSTNTable_Object = MibTable
h3cVoCallHistoryPSTNTable = _H3cVoCallHistoryPSTNTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4)
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryPSTNTable.setStatus("current")
_H3cVoCallHistoryPSTNEntry_Object = MibTableRow
h3cVoCallHistoryPSTNEntry = _H3cVoCallHistoryPSTNEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1)
)
h3cVoCallHistoryPSTNEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisPSTNIndex"),
)
if mibBuilder.loadTexts:
    h3cVoCallHistoryPSTNEntry.setStatus("current")


class _H3cVoCallHisPSTNIndex_Type(Integer32):
    """Custom type h3cVoCallHisPSTNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoCallHisPSTNIndex_Type.__name__ = "Integer32"
_H3cVoCallHisPSTNIndex_Object = MibTableColumn
h3cVoCallHisPSTNIndex = _H3cVoCallHisPSTNIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 1),
    _H3cVoCallHisPSTNIndex_Type()
)
h3cVoCallHisPSTNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNIndex.setStatus("current")
_H3cVoCallHisPSTNSetupTime_Type = DateAndTime
_H3cVoCallHisPSTNSetupTime_Object = MibTableColumn
h3cVoCallHisPSTNSetupTime = _H3cVoCallHisPSTNSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 2),
    _H3cVoCallHisPSTNSetupTime_Type()
)
h3cVoCallHisPSTNSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNSetupTime.setStatus("current")
_H3cVoCallHisPSTNConnTime_Type = DateAndTime
_H3cVoCallHisPSTNConnTime_Object = MibTableColumn
h3cVoCallHisPSTNConnTime = _H3cVoCallHisPSTNConnTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 3),
    _H3cVoCallHisPSTNConnTime_Type()
)
h3cVoCallHisPSTNConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNConnTime.setStatus("current")
_H3cVoCallHisPSTNDiscTime_Type = DateAndTime
_H3cVoCallHisPSTNDiscTime_Object = MibTableColumn
h3cVoCallHisPSTNDiscTime = _H3cVoCallHisPSTNDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 4),
    _H3cVoCallHisPSTNDiscTime_Type()
)
h3cVoCallHisPSTNDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNDiscTime.setStatus("current")
_H3cVoCallHisPSTNTxPackets_Type = Counter32
_H3cVoCallHisPSTNTxPackets_Object = MibTableColumn
h3cVoCallHisPSTNTxPackets = _H3cVoCallHisPSTNTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 5),
    _H3cVoCallHisPSTNTxPackets_Type()
)
h3cVoCallHisPSTNTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNTxPackets.setStatus("current")
_H3cVoCallHisPSTNTxBytes_Type = Counter32
_H3cVoCallHisPSTNTxBytes_Object = MibTableColumn
h3cVoCallHisPSTNTxBytes = _H3cVoCallHisPSTNTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 6),
    _H3cVoCallHisPSTNTxBytes_Type()
)
h3cVoCallHisPSTNTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNTxBytes.setStatus("current")
_H3cVoCallHisPSTNRxPackets_Type = Counter32
_H3cVoCallHisPSTNRxPackets_Object = MibTableColumn
h3cVoCallHisPSTNRxPackets = _H3cVoCallHisPSTNRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 7),
    _H3cVoCallHisPSTNRxPackets_Type()
)
h3cVoCallHisPSTNRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNRxPackets.setStatus("current")
_H3cVoCallHisPSTNRxBytes_Type = Counter32
_H3cVoCallHisPSTNRxBytes_Object = MibTableColumn
h3cVoCallHisPSTNRxBytes = _H3cVoCallHisPSTNRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 8),
    _H3cVoCallHisPSTNRxBytes_Type()
)
h3cVoCallHisPSTNRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHisPSTNRxBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOCALLHISTORY-MIB",
    **{"h3cVoiceCallHistory": h3cVoiceCallHistory,
       "h3cVoCallHistoryObjects": h3cVoCallHistoryObjects,
       "h3cVoCallHistoryMaxLen": h3cVoCallHistoryMaxLen,
       "h3cVoCallHistoryMaxRetainTime": h3cVoCallHistoryMaxRetainTime,
       "h3cVoCallHistoryGenericTable": h3cVoCallHistoryGenericTable,
       "h3cVoCallHistoryGenericEntry": h3cVoCallHistoryGenericEntry,
       "h3cVoCallHisIndex": h3cVoCallHisIndex,
       "h3cVoCallHisCallerNumber": h3cVoCallHisCallerNumber,
       "h3cVoCallHisCalledNumber": h3cVoCallHisCalledNumber,
       "h3cVoCallHisEncodeType": h3cVoCallHisEncodeType,
       "h3cVoCallHisChannel": h3cVoCallHisChannel,
       "h3cVoCallHisLocalAddressType": h3cVoCallHisLocalAddressType,
       "h3cVoCallHisLocalAddress": h3cVoCallHisLocalAddress,
       "h3cVoCallHisPeerAddressType": h3cVoCallHisPeerAddressType,
       "h3cVoCallHisPeerAddress": h3cVoCallHisPeerAddress,
       "h3cVoCallHisDisconnectText": h3cVoCallHisDisconnectText,
       "h3cVoCallHisCallDuration": h3cVoCallHisCallDuration,
       "h3cVoCallHisVoCallDuration": h3cVoCallHisVoCallDuration,
       "h3cVoCallHisFaxCallDuration": h3cVoCallHisFaxCallDuration,
       "h3cVoCallHisImgPages": h3cVoCallHisImgPages,
       "h3cVoCallHisCallOrigin": h3cVoCallHisCallOrigin,
       "h3cVoCallHistoryVoIPTable": h3cVoCallHistoryVoIPTable,
       "h3cVoCallHistoryVoIPEntry": h3cVoCallHistoryVoIPEntry,
       "h3cVoCallHisVoIPIndex": h3cVoCallHisVoIPIndex,
       "h3cVoCallHisVoIPSetupTime": h3cVoCallHisVoIPSetupTime,
       "h3cVoCallHisVoIPConnTime": h3cVoCallHisVoIPConnTime,
       "h3cVoCallHisVoIPDiscTime": h3cVoCallHisVoIPDiscTime,
       "h3cVoCallHisVoIPTxPackets": h3cVoCallHisVoIPTxPackets,
       "h3cVoCallHisVoIPTxBytes": h3cVoCallHisVoIPTxBytes,
       "h3cVoCallHisVoIPRxPackets": h3cVoCallHisVoIPRxPackets,
       "h3cVoCallHisVoIPRxeBytes": h3cVoCallHisVoIPRxeBytes,
       "h3cVoCallHistoryPSTNTable": h3cVoCallHistoryPSTNTable,
       "h3cVoCallHistoryPSTNEntry": h3cVoCallHistoryPSTNEntry,
       "h3cVoCallHisPSTNIndex": h3cVoCallHisPSTNIndex,
       "h3cVoCallHisPSTNSetupTime": h3cVoCallHisPSTNSetupTime,
       "h3cVoCallHisPSTNConnTime": h3cVoCallHisPSTNConnTime,
       "h3cVoCallHisPSTNDiscTime": h3cVoCallHisPSTNDiscTime,
       "h3cVoCallHisPSTNTxPackets": h3cVoCallHisPSTNTxPackets,
       "h3cVoCallHisPSTNTxBytes": h3cVoCallHisPSTNTxBytes,
       "h3cVoCallHisPSTNRxPackets": h3cVoCallHisPSTNRxPackets,
       "h3cVoCallHisPSTNRxBytes": h3cVoCallHisPSTNRxBytes}
)
