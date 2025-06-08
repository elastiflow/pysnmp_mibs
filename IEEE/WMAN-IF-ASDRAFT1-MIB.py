# SNMP MIB module (WMAN-IF-ASDRAFT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/WMAN-IF-ASDRAFT1-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:18:43 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

wmanIfMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VariableMacAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 6),
    )



class WmanIfSfSchedulingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("unsolictedGrantService", 6))
    )



class WmanIfClassifierBitMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("priority", 0),
          ("ipTos", 1),
          ("ipProtocol", 2),
          ("ipMaskedSrcAddr", 3),
          ("ipMaskedDestAddr", 4),
          ("srcPort", 5),
          ("destPort", 6),
          ("destMacAddr", 7),
          ("srcMacAddr", 8),
          ("ethernetProtocol", 9),
          ("userPriority", 10),
          ("vlanId", 11))
    )


class WmanIfOfdmFecCodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("bpskCc1Over2", 0),
          ("qpskRsCcCc1Over2", 1),
          ("qpskRsCcCc3Over4", 2),
          ("sixteenQamRsCcCc1Over2", 3),
          ("sixteenQamRsCcCc3Over4", 4),
          ("sixtyFourQamRsCcCc2Over3", 5),
          ("sixtyFourQamRsCcCc3Over4", 6),
          ("qpskBtc1Over2", 7),
          ("qpskBtc3Over4", 8),
          ("sixteenQamBtc3Over4", 9),
          ("sixteenQamBtc4Over5", 10),
          ("sixtyFourQamBtc2Over3", 11),
          ("sixtyFourQamBtc5Over6", 12),
          ("qpskCtc1Over2", 13),
          ("qpskCtc2Over3", 14),
          ("qpskCtc3Over4", 15),
          ("sixteenQamCtc1Over2", 16),
          ("sixteenQamCtc3Over4", 17),
          ("sixtyFourQamCtc2Over3", 18),
          ("sixtyFourQamCtc3Over4", 19))
    )



# MIB Managed Objects in the order of their OIDs

_WmanIfMibObjects_ObjectIdentity = ObjectIdentity
wmanIfMibObjects = _WmanIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1)
)
_WmanIfBsObjects_ObjectIdentity = ObjectIdentity
wmanIfBsObjects = _WmanIfBsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1)
)
_WmanIfBsPacketCs_ObjectIdentity = ObjectIdentity
wmanIfBsPacketCs = _WmanIfBsPacketCs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1)
)
_WmanIfBsProvisionedSfTable_Object = MibTable
wmanIfBsProvisionedSfTable = _WmanIfBsProvisionedSfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfTable.setStatus("current")
_WmanIfBsProvisionedSfEntry_Object = MibTableRow
wmanIfBsProvisionedSfEntry = _WmanIfBsProvisionedSfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1)
)
wmanIfBsProvisionedSfEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsProvMacAddress"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSfId"),
)
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfEntry.setStatus("current")


class _WmanIfBsSfId_Type(Unsigned32):
    """Custom type wmanIfBsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsSfId_Type.__name__ = "Unsigned32"
_WmanIfBsSfId_Object = MibTableColumn
wmanIfBsSfId = _WmanIfBsSfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 1),
    _WmanIfBsSfId_Type()
)
wmanIfBsSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSfId.setStatus("current")
_WmanIfBsSsProvMacAddress_Type = VariableMacAddress
_WmanIfBsSsProvMacAddress_Object = MibTableColumn
wmanIfBsSsProvMacAddress = _WmanIfBsSsProvMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 2),
    _WmanIfBsSsProvMacAddress_Type()
)
wmanIfBsSsProvMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsProvMacAddress.setStatus("current")


class _WmanIfBsSfDirection_Type(Integer32):
    """Custom type wmanIfBsSfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_WmanIfBsSfDirection_Type.__name__ = "Integer32"
_WmanIfBsSfDirection_Object = MibTableColumn
wmanIfBsSfDirection = _WmanIfBsSfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 3),
    _WmanIfBsSfDirection_Type()
)
wmanIfBsSfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfDirection.setStatus("current")
_WmanIfBsServiceClassIndex_Type = Integer32
_WmanIfBsServiceClassIndex_Object = MibTableColumn
wmanIfBsServiceClassIndex = _WmanIfBsServiceClassIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 4),
    _WmanIfBsServiceClassIndex_Type()
)
wmanIfBsServiceClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsServiceClassIndex.setStatus("current")


class _WmanIfBsServiceClassName_Type(DisplayString):
    """Custom type wmanIfBsServiceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WmanIfBsServiceClassName_Type.__name__ = "DisplayString"
_WmanIfBsServiceClassName_Object = MibTableColumn
wmanIfBsServiceClassName = _WmanIfBsServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 5),
    _WmanIfBsServiceClassName_Type()
)
wmanIfBsServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsServiceClassName.setStatus("current")


class _WmanIfBsSfState_Type(Integer32):
    """Custom type wmanIfBsSfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provisioned", 1),
          ("admitted", 2),
          ("active", 3))
    )


_WmanIfBsSfState_Type.__name__ = "Integer32"
_WmanIfBsSfState_Object = MibTableColumn
wmanIfBsSfState = _WmanIfBsSfState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 6),
    _WmanIfBsSfState_Type()
)
wmanIfBsSfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfState.setStatus("current")
_WmanIfBsSfProvisionedTime_Type = TimeStamp
_WmanIfBsSfProvisionedTime_Object = MibTableColumn
wmanIfBsSfProvisionedTime = _WmanIfBsSfProvisionedTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 7),
    _WmanIfBsSfProvisionedTime_Type()
)
wmanIfBsSfProvisionedTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsSfProvisionedTime.setStatus("current")
_WmanIfBsProvisionedSfRowStatus_Type = RowStatus
_WmanIfBsProvisionedSfRowStatus_Object = MibTableColumn
wmanIfBsProvisionedSfRowStatus = _WmanIfBsProvisionedSfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 1, 1, 8),
    _WmanIfBsProvisionedSfRowStatus_Type()
)
wmanIfBsProvisionedSfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsProvisionedSfRowStatus.setStatus("current")
_WmanIfBsServiceClassTable_Object = MibTable
wmanIfBsServiceClassTable = _WmanIfBsServiceClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsServiceClassTable.setStatus("current")
_WmanIfBsServiceClassEntry_Object = MibTableRow
wmanIfBsServiceClassEntry = _WmanIfBsServiceClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1)
)
wmanIfBsServiceClassEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsQoSProfileIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsServiceClassEntry.setStatus("current")


class _WmanIfBsQoSProfileIndex_Type(Integer32):
    """Custom type wmanIfBsQoSProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WmanIfBsQoSProfileIndex_Type.__name__ = "Integer32"
_WmanIfBsQoSProfileIndex_Object = MibTableColumn
wmanIfBsQoSProfileIndex = _WmanIfBsQoSProfileIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 1),
    _WmanIfBsQoSProfileIndex_Type()
)
wmanIfBsQoSProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsQoSProfileIndex.setStatus("current")


class _WmanIfBsQosServiceClassName_Type(DisplayString):
    """Custom type wmanIfBsQosServiceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WmanIfBsQosServiceClassName_Type.__name__ = "DisplayString"
_WmanIfBsQosServiceClassName_Object = MibTableColumn
wmanIfBsQosServiceClassName = _WmanIfBsQosServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 2),
    _WmanIfBsQosServiceClassName_Type()
)
wmanIfBsQosServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosServiceClassName.setStatus("current")


class _WmanIfBsQoSTrafficPriority_Type(Integer32):
    """Custom type wmanIfBsQoSTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsQoSTrafficPriority_Type.__name__ = "Integer32"
_WmanIfBsQoSTrafficPriority_Object = MibTableColumn
wmanIfBsQoSTrafficPriority = _WmanIfBsQoSTrafficPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 3),
    _WmanIfBsQoSTrafficPriority_Type()
)
wmanIfBsQoSTrafficPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSTrafficPriority.setStatus("current")
_WmanIfBsQoSMaxSustainedRate_Type = Integer32
_WmanIfBsQoSMaxSustainedRate_Object = MibTableColumn
wmanIfBsQoSMaxSustainedRate = _WmanIfBsQoSMaxSustainedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 4),
    _WmanIfBsQoSMaxSustainedRate_Type()
)
wmanIfBsQoSMaxSustainedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxSustainedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxSustainedRate.setUnits("bps")
_WmanIfBsQoSMaxTrafficBurst_Type = Integer32
_WmanIfBsQoSMaxTrafficBurst_Object = MibTableColumn
wmanIfBsQoSMaxTrafficBurst = _WmanIfBsQoSMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 5),
    _WmanIfBsQoSMaxTrafficBurst_Type()
)
wmanIfBsQoSMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxTrafficBurst.setUnits("byte")
_WmanIfBsQoSMinReservedRate_Type = Integer32
_WmanIfBsQoSMinReservedRate_Object = MibTableColumn
wmanIfBsQoSMinReservedRate = _WmanIfBsQoSMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 6),
    _WmanIfBsQoSMinReservedRate_Type()
)
wmanIfBsQoSMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMinReservedRate.setUnits("bps")
_WmanIfBsQoSToleratedJitter_Type = Integer32
_WmanIfBsQoSToleratedJitter_Object = MibTableColumn
wmanIfBsQoSToleratedJitter = _WmanIfBsQoSToleratedJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 7),
    _WmanIfBsQoSToleratedJitter_Type()
)
wmanIfBsQoSToleratedJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSToleratedJitter.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSToleratedJitter.setUnits("millisecond")
_WmanIfBsQoSMaxLatency_Type = Integer32
_WmanIfBsQoSMaxLatency_Object = MibTableColumn
wmanIfBsQoSMaxLatency = _WmanIfBsQoSMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 8),
    _WmanIfBsQoSMaxLatency_Type()
)
wmanIfBsQoSMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSMaxLatency.setUnits("millisecond")


class _WmanIfBsQoSFixedVsVariableSduInd_Type(Integer32):
    """Custom type wmanIfBsQoSFixedVsVariableSduInd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("variableLength", 0),
          ("fixedLength", 1))
    )


_WmanIfBsQoSFixedVsVariableSduInd_Type.__name__ = "Integer32"
_WmanIfBsQoSFixedVsVariableSduInd_Object = MibTableColumn
wmanIfBsQoSFixedVsVariableSduInd = _WmanIfBsQoSFixedVsVariableSduInd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 9),
    _WmanIfBsQoSFixedVsVariableSduInd_Type()
)
wmanIfBsQoSFixedVsVariableSduInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSFixedVsVariableSduInd.setStatus("current")


class _WmanIfBsQoSSduSize_Type(Integer32):
    """Custom type wmanIfBsQoSSduSize based on Integer32"""
    defaultValue = 49


_WmanIfBsQoSSduSize_Type.__name__ = "Integer32"
_WmanIfBsQoSSduSize_Object = MibTableColumn
wmanIfBsQoSSduSize = _WmanIfBsQoSSduSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 10),
    _WmanIfBsQoSSduSize_Type()
)
wmanIfBsQoSSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSSduSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQoSSduSize.setUnits("byte")


class _WmanIfBsQosScSchedulingType_Type(WmanIfSfSchedulingType):
    """Custom type wmanIfBsQosScSchedulingType based on WmanIfSfSchedulingType"""
    defaultValue = 2


_WmanIfBsQosScSchedulingType_Type.__name__ = "WmanIfSfSchedulingType"
_WmanIfBsQosScSchedulingType_Object = MibTableColumn
wmanIfBsQosScSchedulingType = _WmanIfBsQosScSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 11),
    _WmanIfBsQosScSchedulingType_Type()
)
wmanIfBsQosScSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScSchedulingType.setStatus("current")
_WmanIfBsQosScArqEnable_Type = TruthValue
_WmanIfBsQosScArqEnable_Object = MibTableColumn
wmanIfBsQosScArqEnable = _WmanIfBsQosScArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 12),
    _WmanIfBsQosScArqEnable_Type()
)
wmanIfBsQosScArqEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqEnable.setStatus("current")


class _WmanIfBsQosScArqWindowSize_Type(Integer32):
    """Custom type wmanIfBsQosScArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfBsQosScArqWindowSize_Type.__name__ = "Integer32"
_WmanIfBsQosScArqWindowSize_Object = MibTableColumn
wmanIfBsQosScArqWindowSize = _WmanIfBsQosScArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 13),
    _WmanIfBsQosScArqWindowSize_Type()
)
wmanIfBsQosScArqWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqWindowSize.setStatus("current")


class _WmanIfBsQosScArqFragmentLifetime_Type(Integer32):
    """Custom type wmanIfBsQosScArqFragmentLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqFragmentLifetime_Type.__name__ = "Integer32"
_WmanIfBsQosScArqFragmentLifetime_Object = MibTableColumn
wmanIfBsQosScArqFragmentLifetime = _WmanIfBsQosScArqFragmentLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 14),
    _WmanIfBsQosScArqFragmentLifetime_Type()
)
wmanIfBsQosScArqFragmentLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqFragmentLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqFragmentLifetime.setUnits("10 us")


class _WmanIfBsQosScArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfBsQosScArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfBsQosScArqSyncLossTimeout_Object = MibTableColumn
wmanIfBsQosScArqSyncLossTimeout = _WmanIfBsQosScArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 15),
    _WmanIfBsQosScArqSyncLossTimeout_Type()
)
wmanIfBsQosScArqSyncLossTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqSyncLossTimeout.setUnits("10 us")
_WmanIfBsQosScArqDeliverInOrder_Type = TruthValue
_WmanIfBsQosScArqDeliverInOrder_Object = MibTableColumn
wmanIfBsQosScArqDeliverInOrder = _WmanIfBsQosScArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 16),
    _WmanIfBsQosScArqDeliverInOrder_Type()
)
wmanIfBsQosScArqDeliverInOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqDeliverInOrder.setStatus("current")


class _WmanIfBsQosScArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfBsQosScArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsQosScArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfBsQosScArqRxPurgeTimeout_Object = MibTableColumn
wmanIfBsQosScArqRxPurgeTimeout = _WmanIfBsQosScArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 17),
    _WmanIfBsQosScArqRxPurgeTimeout_Type()
)
wmanIfBsQosScArqRxPurgeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfBsQosScArqBlockSize_Type(Integer32):
    """Custom type wmanIfBsQosScArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIfBsQosScArqBlockSize_Type.__name__ = "Integer32"
_WmanIfBsQosScArqBlockSize_Object = MibTableColumn
wmanIfBsQosScArqBlockSize = _WmanIfBsQosScArqBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 18),
    _WmanIfBsQosScArqBlockSize_Type()
)
wmanIfBsQosScArqBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosScArqBlockSize.setUnits("byte")
_WmanIfBsQosSCMinRsvdTolerableRate_Type = Integer32
_WmanIfBsQosSCMinRsvdTolerableRate_Object = MibTableColumn
wmanIfBsQosSCMinRsvdTolerableRate = _WmanIfBsQosSCMinRsvdTolerableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 19),
    _WmanIfBsQosSCMinRsvdTolerableRate_Type()
)
wmanIfBsQosSCMinRsvdTolerableRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQosSCMinRsvdTolerableRate.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsQosSCMinRsvdTolerableRate.setUnits("bps")


class _WmanIfBsQoSReqTxPolicy_Type(Bits):
    """Custom type wmanIfBsQoSReqTxPolicy based on Bits"""
    namedValues = NamedValues(
        *(("noBroadcastBwReq", 0),
          ("reserved1", 1),
          ("noPiggybackReq", 2),
          ("noFragmentData", 3),
          ("noPHS", 4),
          ("noSduPacking", 5),
          ("noCrc", 6),
          ("reserved2", 7))
    )

_WmanIfBsQoSReqTxPolicy_Type.__name__ = "Bits"
_WmanIfBsQoSReqTxPolicy_Object = MibTableColumn
wmanIfBsQoSReqTxPolicy = _WmanIfBsQoSReqTxPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 20),
    _WmanIfBsQoSReqTxPolicy_Type()
)
wmanIfBsQoSReqTxPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSReqTxPolicy.setStatus("current")
_WmanIfBsQoSServiceClassRowStatus_Type = RowStatus
_WmanIfBsQoSServiceClassRowStatus_Object = MibTableColumn
wmanIfBsQoSServiceClassRowStatus = _WmanIfBsQoSServiceClassRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 2, 1, 21),
    _WmanIfBsQoSServiceClassRowStatus_Type()
)
wmanIfBsQoSServiceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsQoSServiceClassRowStatus.setStatus("current")
_WmanIfBsClassifierRuleTable_Object = MibTable
wmanIfBsClassifierRuleTable = _WmanIfBsClassifierRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleTable.setStatus("current")
_WmanIfBsClassifierRuleEntry_Object = MibTableRow
wmanIfBsClassifierRuleEntry = _WmanIfBsClassifierRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1)
)
wmanIfBsClassifierRuleEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSfIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsClassifierRuleIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEntry.setStatus("current")


class _WmanIfBsSfIndex_Type(Unsigned32):
    """Custom type wmanIfBsSfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsSfIndex_Type.__name__ = "Unsigned32"
_WmanIfBsSfIndex_Object = MibTableColumn
wmanIfBsSfIndex = _WmanIfBsSfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 1),
    _WmanIfBsSfIndex_Type()
)
wmanIfBsSfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSfIndex.setStatus("current")


class _WmanIfBsClassifierRuleIndex_Type(Unsigned32):
    """Custom type wmanIfBsClassifierRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsClassifierRuleIndex_Type.__name__ = "Unsigned32"
_WmanIfBsClassifierRuleIndex_Object = MibTableColumn
wmanIfBsClassifierRuleIndex = _WmanIfBsClassifierRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 2),
    _WmanIfBsClassifierRuleIndex_Type()
)
wmanIfBsClassifierRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIndex.setStatus("current")


class _WmanIfBsClassifierRulePriority_Type(Integer32):
    """Custom type wmanIfBsClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIfBsClassifierRulePriority_Object = MibTableColumn
wmanIfBsClassifierRulePriority = _WmanIfBsClassifierRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 3),
    _WmanIfBsClassifierRulePriority_Type()
)
wmanIfBsClassifierRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePriority.setStatus("current")


class _WmanIfBsClassifierRuleIpTosLow_Type(OctetString):
    """Custom type wmanIfBsClassifierRuleIpTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfBsClassifierRuleIpTosLow_Type.__name__ = "OctetString"
_WmanIfBsClassifierRuleIpTosLow_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosLow = _WmanIfBsClassifierRuleIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 4),
    _WmanIfBsClassifierRuleIpTosLow_Type()
)
wmanIfBsClassifierRuleIpTosLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosLow.setStatus("current")


class _WmanIfBsClassifierRuleIpTosHigh_Type(OctetString):
    """Custom type wmanIfBsClassifierRuleIpTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfBsClassifierRuleIpTosHigh_Type.__name__ = "OctetString"
_WmanIfBsClassifierRuleIpTosHigh_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosHigh = _WmanIfBsClassifierRuleIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 5),
    _WmanIfBsClassifierRuleIpTosHigh_Type()
)
wmanIfBsClassifierRuleIpTosHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosHigh.setStatus("current")


class _WmanIfBsClassifierRuleIpTosMask_Type(OctetString):
    """Custom type wmanIfBsClassifierRuleIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfBsClassifierRuleIpTosMask_Type.__name__ = "OctetString"
_WmanIfBsClassifierRuleIpTosMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpTosMask = _WmanIfBsClassifierRuleIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 6),
    _WmanIfBsClassifierRuleIpTosMask_Type()
)
wmanIfBsClassifierRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpTosMask.setStatus("current")


class _WmanIfBsClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleIpProtocol_Object = MibTableColumn
wmanIfBsClassifierRuleIpProtocol = _WmanIfBsClassifierRuleIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 7),
    _WmanIfBsClassifierRuleIpProtocol_Type()
)
wmanIfBsClassifierRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpProtocol.setStatus("current")
_WmanIfBsClassifierRuleIpAddressType_Type = InetAddressType
_WmanIfBsClassifierRuleIpAddressType_Object = MibTableColumn
wmanIfBsClassifierRuleIpAddressType = _WmanIfBsClassifierRuleIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 8),
    _WmanIfBsClassifierRuleIpAddressType_Type()
)
wmanIfBsClassifierRuleIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpAddressType.setStatus("current")
_WmanIfBsClassifierRuleIpSourceAddr_Type = InetAddress
_WmanIfBsClassifierRuleIpSourceAddr_Object = MibTableColumn
wmanIfBsClassifierRuleIpSourceAddr = _WmanIfBsClassifierRuleIpSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 9),
    _WmanIfBsClassifierRuleIpSourceAddr_Type()
)
wmanIfBsClassifierRuleIpSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpSourceAddr.setStatus("current")
_WmanIfBsClassifierRuleIpSourceMask_Type = InetAddress
_WmanIfBsClassifierRuleIpSourceMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpSourceMask = _WmanIfBsClassifierRuleIpSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 10),
    _WmanIfBsClassifierRuleIpSourceMask_Type()
)
wmanIfBsClassifierRuleIpSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpSourceMask.setStatus("current")
_WmanIfBsClassifierRuleIpDestAddr_Type = InetAddress
_WmanIfBsClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIfBsClassifierRuleIpDestAddr = _WmanIfBsClassifierRuleIpDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 11),
    _WmanIfBsClassifierRuleIpDestAddr_Type()
)
wmanIfBsClassifierRuleIpDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpDestAddr.setStatus("current")
_WmanIfBsClassifierRuleIpDestMask_Type = InetAddress
_WmanIfBsClassifierRuleIpDestMask_Object = MibTableColumn
wmanIfBsClassifierRuleIpDestMask = _WmanIfBsClassifierRuleIpDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 12),
    _WmanIfBsClassifierRuleIpDestMask_Type()
)
wmanIfBsClassifierRuleIpDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleIpDestMask.setStatus("current")


class _WmanIfBsClassifierRuleSourcePortStart_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleSourcePortStart_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleSourcePortStart_Object = MibTableColumn
wmanIfBsClassifierRuleSourcePortStart = _WmanIfBsClassifierRuleSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 13),
    _WmanIfBsClassifierRuleSourcePortStart_Type()
)
wmanIfBsClassifierRuleSourcePortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourcePortStart.setStatus("current")


class _WmanIfBsClassifierRuleSourcePortEnd_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleSourcePortEnd_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleSourcePortEnd_Object = MibTableColumn
wmanIfBsClassifierRuleSourcePortEnd = _WmanIfBsClassifierRuleSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 14),
    _WmanIfBsClassifierRuleSourcePortEnd_Type()
)
wmanIfBsClassifierRuleSourcePortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourcePortEnd.setStatus("current")


class _WmanIfBsClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleDestPortStart_Object = MibTableColumn
wmanIfBsClassifierRuleDestPortStart = _WmanIfBsClassifierRuleDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 15),
    _WmanIfBsClassifierRuleDestPortStart_Type()
)
wmanIfBsClassifierRuleDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestPortStart.setStatus("current")


class _WmanIfBsClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIfBsClassifierRuleDestPortEnd = _WmanIfBsClassifierRuleDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 16),
    _WmanIfBsClassifierRuleDestPortEnd_Type()
)
wmanIfBsClassifierRuleDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestPortEnd.setStatus("current")
_WmanIfBsClassifierRuleDestMacAddr_Type = MacAddress
_WmanIfBsClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIfBsClassifierRuleDestMacAddr = _WmanIfBsClassifierRuleDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 17),
    _WmanIfBsClassifierRuleDestMacAddr_Type()
)
wmanIfBsClassifierRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestMacAddr.setStatus("current")
_WmanIfBsClassifierRuleDestMacMask_Type = MacAddress
_WmanIfBsClassifierRuleDestMacMask_Object = MibTableColumn
wmanIfBsClassifierRuleDestMacMask = _WmanIfBsClassifierRuleDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 18),
    _WmanIfBsClassifierRuleDestMacMask_Type()
)
wmanIfBsClassifierRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleDestMacMask.setStatus("current")
_WmanIfBsClassifierRuleSourceMacAddr_Type = MacAddress
_WmanIfBsClassifierRuleSourceMacAddr_Object = MibTableColumn
wmanIfBsClassifierRuleSourceMacAddr = _WmanIfBsClassifierRuleSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 19),
    _WmanIfBsClassifierRuleSourceMacAddr_Type()
)
wmanIfBsClassifierRuleSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourceMacAddr.setStatus("current")
_WmanIfBsClassifierRuleSourceMacMask_Type = MacAddress
_WmanIfBsClassifierRuleSourceMacMask_Object = MibTableColumn
wmanIfBsClassifierRuleSourceMacMask = _WmanIfBsClassifierRuleSourceMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 20),
    _WmanIfBsClassifierRuleSourceMacMask_Type()
)
wmanIfBsClassifierRuleSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleSourceMacMask.setStatus("current")


class _WmanIfBsClassifierRuleEnetProtocolType_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleEnetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ethertype", 1),
          ("dsap", 2))
    )


_WmanIfBsClassifierRuleEnetProtocolType_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleEnetProtocolType_Object = MibTableColumn
wmanIfBsClassifierRuleEnetProtocolType = _WmanIfBsClassifierRuleEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 21),
    _WmanIfBsClassifierRuleEnetProtocolType_Type()
)
wmanIfBsClassifierRuleEnetProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEnetProtocolType.setStatus("current")


class _WmanIfBsClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIfBsClassifierRuleEnetProtocol = _WmanIfBsClassifierRuleEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 22),
    _WmanIfBsClassifierRuleEnetProtocol_Type()
)
wmanIfBsClassifierRuleEnetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleEnetProtocol.setStatus("current")


class _WmanIfBsClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleUserPriLow_Object = MibTableColumn
wmanIfBsClassifierRuleUserPriLow = _WmanIfBsClassifierRuleUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 23),
    _WmanIfBsClassifierRuleUserPriLow_Type()
)
wmanIfBsClassifierRuleUserPriLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleUserPriLow.setStatus("current")


class _WmanIfBsClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfBsClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIfBsClassifierRuleUserPriHigh = _WmanIfBsClassifierRuleUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 24),
    _WmanIfBsClassifierRuleUserPriHigh_Type()
)
wmanIfBsClassifierRuleUserPriHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleUserPriHigh.setStatus("current")


class _WmanIfBsClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIfBsClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleVlanId_Object = MibTableColumn
wmanIfBsClassifierRuleVlanId = _WmanIfBsClassifierRuleVlanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 25),
    _WmanIfBsClassifierRuleVlanId_Type()
)
wmanIfBsClassifierRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleVlanId.setStatus("current")


class _WmanIfBsClassifierRuleState_Type(Integer32):
    """Custom type wmanIfBsClassifierRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WmanIfBsClassifierRuleState_Type.__name__ = "Integer32"
_WmanIfBsClassifierRuleState_Object = MibTableColumn
wmanIfBsClassifierRuleState = _WmanIfBsClassifierRuleState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 26),
    _WmanIfBsClassifierRuleState_Type()
)
wmanIfBsClassifierRuleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleState.setStatus("current")
_WmanIfBsClassifierRulePkts_Type = Counter64
_WmanIfBsClassifierRulePkts_Object = MibTableColumn
wmanIfBsClassifierRulePkts = _WmanIfBsClassifierRulePkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 27),
    _WmanIfBsClassifierRulePkts_Type()
)
wmanIfBsClassifierRulePkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRulePkts.setStatus("current")
_WmanIfBSClassifierRuleBitMap_Type = WmanIfClassifierBitMap
_WmanIfBSClassifierRuleBitMap_Object = MibTableColumn
wmanIfBSClassifierRuleBitMap = _WmanIfBSClassifierRuleBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 28),
    _WmanIfBSClassifierRuleBitMap_Type()
)
wmanIfBSClassifierRuleBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBSClassifierRuleBitMap.setStatus("current")
_WmanIfBsClassifierRuleRowStatus_Type = RowStatus
_WmanIfBsClassifierRuleRowStatus_Object = MibTableColumn
wmanIfBsClassifierRuleRowStatus = _WmanIfBsClassifierRuleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 3, 1, 29),
    _WmanIfBsClassifierRuleRowStatus_Type()
)
wmanIfBsClassifierRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfBsClassifierRuleRowStatus.setStatus("current")
_WmanIfBsSsPacketCounterTable_Object = MibTable
wmanIfBsSsPacketCounterTable = _WmanIfBsSsPacketCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wmanIfBsSsPacketCounterTable.setStatus("current")
_WmanIfBsSsPacketCounterEntry_Object = MibTableRow
wmanIfBsSsPacketCounterEntry = _WmanIfBsSsPacketCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1)
)
wmanIfBsSsPacketCounterEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsSfIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsPktMacAddr"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsPacketCounterEntry.setStatus("current")


class _WmanIfBsSsSfIndex_Type(Unsigned32):
    """Custom type wmanIfBsSsSfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsSsSfIndex_Type.__name__ = "Unsigned32"
_WmanIfBsSsSfIndex_Object = MibTableColumn
wmanIfBsSsSfIndex = _WmanIfBsSsSfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 1),
    _WmanIfBsSsSfIndex_Type()
)
wmanIfBsSsSfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsSfIndex.setStatus("current")
_WmanIfBsSsPktMacAddr_Type = VariableMacAddress
_WmanIfBsSsPktMacAddr_Object = MibTableColumn
wmanIfBsSsPktMacAddr = _WmanIfBsSsPktMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 2),
    _WmanIfBsSsPktMacAddr_Type()
)
wmanIfBsSsPktMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsPktMacAddr.setStatus("current")


class _WmanIfBsSsSfDirection_Type(Integer32):
    """Custom type wmanIfBsSsSfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("receive", 2))
    )


_WmanIfBsSsSfDirection_Type.__name__ = "Integer32"
_WmanIfBsSsSfDirection_Object = MibTableColumn
wmanIfBsSsSfDirection = _WmanIfBsSsSfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 3),
    _WmanIfBsSsSfDirection_Type()
)
wmanIfBsSsSfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsSfDirection.setStatus("current")
_WmanIfBsSsMacSduCount_Type = Counter64
_WmanIfBsSsMacSduCount_Object = MibTableColumn
wmanIfBsSsMacSduCount = _WmanIfBsSsMacSduCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 4),
    _WmanIfBsSsMacSduCount_Type()
)
wmanIfBsSsMacSduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacSduCount.setStatus("current")
_WmanIfBsSsOctetCount_Type = Counter64
_WmanIfBsSsOctetCount_Object = MibTableColumn
wmanIfBsSsOctetCount = _WmanIfBsSsOctetCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 5),
    _WmanIfBsSsOctetCount_Type()
)
wmanIfBsSsOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsOctetCount.setStatus("current")


class _WmanIfBsSsResetCounter_Type(Integer32):
    """Custom type wmanIfBsSsResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("resetCounter", 1))
    )


_WmanIfBsSsResetCounter_Type.__name__ = "Integer32"
_WmanIfBsSsResetCounter_Object = MibTableColumn
wmanIfBsSsResetCounter = _WmanIfBsSsResetCounter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 6),
    _WmanIfBsSsResetCounter_Type()
)
wmanIfBsSsResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsResetCounter.setStatus("current")
_WmanIfBsSsResetCounterTime_Type = TimeStamp
_WmanIfBsSsResetCounterTime_Object = MibTableColumn
wmanIfBsSsResetCounterTime = _WmanIfBsSsResetCounterTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 1, 4, 1, 7),
    _WmanIfBsSsResetCounterTime_Type()
)
wmanIfBsSsResetCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsResetCounterTime.setStatus("current")
_WmanIfBsCps_ObjectIdentity = ObjectIdentity
wmanIfBsCps = _WmanIfBsCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2)
)
_WmanIfBsRegisteredSsTable_Object = MibTable
wmanIfBsRegisteredSsTable = _WmanIfBsRegisteredSsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsRegisteredSsTable.setStatus("current")
_WmanIfBsRegisteredSsEntry_Object = MibTableRow
wmanIfBsRegisteredSsEntry = _WmanIfBsRegisteredSsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1)
)
wmanIfBsRegisteredSsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsIdIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsRegisteredSsEntry.setStatus("current")


class _WmanIfBsSsIdIndex_Type(Unsigned32):
    """Custom type wmanIfBsSsIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsSsIdIndex_Type.__name__ = "Unsigned32"
_WmanIfBsSsIdIndex_Object = MibTableColumn
wmanIfBsSsIdIndex = _WmanIfBsSsIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 1),
    _WmanIfBsSsIdIndex_Type()
)
wmanIfBsSsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsSsIdIndex.setStatus("current")
_WmanIfBsSsMacAddress_Type = MacAddress
_WmanIfBsSsMacAddress_Object = MibTableColumn
wmanIfBsSsMacAddress = _WmanIfBsSsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 2),
    _WmanIfBsSsMacAddress_Type()
)
wmanIfBsSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacAddress.setStatus("current")
_WmanIfBsSsBasicCid_Type = Integer32
_WmanIfBsSsBasicCid_Object = MibTableColumn
wmanIfBsSsBasicCid = _WmanIfBsSsBasicCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 3),
    _WmanIfBsSsBasicCid_Type()
)
wmanIfBsSsBasicCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsBasicCid.setStatus("current")
_WmanIfBsSsPrimaryCid_Type = Integer32
_WmanIfBsSsPrimaryCid_Object = MibTableColumn
wmanIfBsSsPrimaryCid = _WmanIfBsSsPrimaryCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 4),
    _WmanIfBsSsPrimaryCid_Type()
)
wmanIfBsSsPrimaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPrimaryCid.setStatus("current")
_WmanIfBsSsSecondaryCid_Type = Integer32
_WmanIfBsSsSecondaryCid_Object = MibTableColumn
wmanIfBsSsSecondaryCid = _WmanIfBsSsSecondaryCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 5),
    _WmanIfBsSsSecondaryCid_Type()
)
wmanIfBsSsSecondaryCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsSecondaryCid.setStatus("current")
_WmanIfBsSsHmacTuple_Type = OctetString
_WmanIfBsSsHmacTuple_Object = MibTableColumn
wmanIfBsSsHmacTuple = _WmanIfBsSsHmacTuple_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 6),
    _WmanIfBsSsHmacTuple_Type()
)
wmanIfBsSsHmacTuple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsHmacTuple.setStatus("current")
_WmanIfBsSsUlCidSupport_Type = Integer32
_WmanIfBsSsUlCidSupport_Object = MibTableColumn
wmanIfBsSsUlCidSupport = _WmanIfBsSsUlCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 7),
    _WmanIfBsSsUlCidSupport_Type()
)
wmanIfBsSsUlCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsUlCidSupport.setStatus("current")


class _WmanIfBsSsManagementSupport_Type(Integer32):
    """Custom type wmanIfBsSsManagementSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmanagedSs", 0),
          ("managedSs", 1))
    )


_WmanIfBsSsManagementSupport_Type.__name__ = "Integer32"
_WmanIfBsSsManagementSupport_Object = MibTableColumn
wmanIfBsSsManagementSupport = _WmanIfBsSsManagementSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 8),
    _WmanIfBsSsManagementSupport_Type()
)
wmanIfBsSsManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsManagementSupport.setStatus("current")


class _WmanIfBsSsArqSupport_Type(Integer32):
    """Custom type wmanIfBsSsArqSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arqNotSupported", 0),
          ("arqSupported", 1))
    )


_WmanIfBsSsArqSupport_Type.__name__ = "Integer32"
_WmanIfBsSsArqSupport_Object = MibTableColumn
wmanIfBsSsArqSupport = _WmanIfBsSsArqSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 9),
    _WmanIfBsSsArqSupport_Type()
)
wmanIfBsSsArqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsArqSupport.setStatus("current")


class _WmanIfBsSsDsxFlowControl_Type(Integer32):
    """Custom type wmanIfBsSsDsxFlowControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsSsDsxFlowControl_Type.__name__ = "Integer32"
_WmanIfBsSsDsxFlowControl_Object = MibTableColumn
wmanIfBsSsDsxFlowControl = _WmanIfBsSsDsxFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 10),
    _WmanIfBsSsDsxFlowControl_Type()
)
wmanIfBsSsDsxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsDsxFlowControl.setStatus("current")


class _WmanIfBsSsMacCrcSupport_Type(Integer32):
    """Custom type wmanIfBsSsMacCrcSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noMacCrcSupport", 0),
          ("macCrcSupport", 1))
    )


_WmanIfBsSsMacCrcSupport_Type.__name__ = "Integer32"
_WmanIfBsSsMacCrcSupport_Object = MibTableColumn
wmanIfBsSsMacCrcSupport = _WmanIfBsSsMacCrcSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 11),
    _WmanIfBsSsMacCrcSupport_Type()
)
wmanIfBsSsMacCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacCrcSupport.setStatus("current")


class _WmanIfBsSsMcaFlowControl_Type(Integer32):
    """Custom type wmanIfBsSsMcaFlowControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsSsMcaFlowControl_Type.__name__ = "Integer32"
_WmanIfBsSsMcaFlowControl_Object = MibTableColumn
wmanIfBsSsMcaFlowControl = _WmanIfBsSsMcaFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 12),
    _WmanIfBsSsMcaFlowControl_Type()
)
wmanIfBsSsMcaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMcaFlowControl.setStatus("current")


class _WmanIfBsSsMcpGroupCidSupport_Type(Integer32):
    """Custom type wmanIfBsSsMcpGroupCidSupport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsSsMcpGroupCidSupport_Type.__name__ = "Integer32"
_WmanIfBsSsMcpGroupCidSupport_Object = MibTableColumn
wmanIfBsSsMcpGroupCidSupport = _WmanIfBsSsMcpGroupCidSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 13),
    _WmanIfBsSsMcpGroupCidSupport_Type()
)
wmanIfBsSsMcpGroupCidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMcpGroupCidSupport.setStatus("current")


class _WmanIfBsSsPkmFlowControl_Type(Integer32):
    """Custom type wmanIfBsSsPkmFlowControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsSsPkmFlowControl_Type.__name__ = "Integer32"
_WmanIfBsSsPkmFlowControl_Object = MibTableColumn
wmanIfBsSsPkmFlowControl = _WmanIfBsSsPkmFlowControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 14),
    _WmanIfBsSsPkmFlowControl_Type()
)
wmanIfBsSsPkmFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPkmFlowControl.setStatus("current")


class _WmanIfBsSsAuthorizationPolicyControl_Type(Bits):
    """Custom type wmanIfBsSsAuthorizationPolicyControl based on Bits"""
    namedValues = NamedValues(
        *(("ieee802-16PrivacySupported", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7))
    )

_WmanIfBsSsAuthorizationPolicyControl_Type.__name__ = "Bits"
_WmanIfBsSsAuthorizationPolicyControl_Object = MibTableColumn
wmanIfBsSsAuthorizationPolicyControl = _WmanIfBsSsAuthorizationPolicyControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 15),
    _WmanIfBsSsAuthorizationPolicyControl_Type()
)
wmanIfBsSsAuthorizationPolicyControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsAuthorizationPolicyControl.setStatus("current")


class _WmanIfBsSsMaxNumOfSupportedSA_Type(Integer32):
    """Custom type wmanIfBsSsMaxNumOfSupportedSA based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfBsSsMaxNumOfSupportedSA_Type.__name__ = "Integer32"
_WmanIfBsSsMaxNumOfSupportedSA_Object = MibTableColumn
wmanIfBsSsMaxNumOfSupportedSA = _WmanIfBsSsMaxNumOfSupportedSA_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 16),
    _WmanIfBsSsMaxNumOfSupportedSA_Type()
)
wmanIfBsSsMaxNumOfSupportedSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxNumOfSupportedSA.setStatus("current")


class _WmanIfBsSsIpVersion_Type(Integer32):
    """Custom type wmanIfBsSsIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_WmanIfBsSsIpVersion_Type.__name__ = "Integer32"
_WmanIfBsSsIpVersion_Object = MibTableColumn
wmanIfBsSsIpVersion = _WmanIfBsSsIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 17),
    _WmanIfBsSsIpVersion_Type()
)
wmanIfBsSsIpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsIpVersion.setStatus("current")


class _WmanIfBsSsMacCsSupportBitMap_Type(Bits):
    """Custom type wmanIfBsSsMacCsSupportBitMap based on Bits"""
    namedValues = NamedValues(
        *(("atm", 0),
          ("packetIpv4", 1),
          ("packetIpv6", 2),
          ("packet802-3", 3),
          ("packet802-1Q", 4),
          ("packetIpv4Over802-3", 5),
          ("packetIpv6Over802-3", 6),
          ("packetIpv4Over802-1Q", 7),
          ("packetIpv6Over802-1Q", 8))
    )

_WmanIfBsSsMacCsSupportBitMap_Type.__name__ = "Bits"
_WmanIfBsSsMacCsSupportBitMap_Object = MibTableColumn
wmanIfBsSsMacCsSupportBitMap = _WmanIfBsSsMacCsSupportBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 18),
    _WmanIfBsSsMacCsSupportBitMap_Type()
)
wmanIfBsSsMacCsSupportBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMacCsSupportBitMap.setStatus("current")


class _WmanIfBsSsMaxNumOfClassifier_Type(Integer32):
    """Custom type wmanIfBsSsMaxNumOfClassifier based on Integer32"""
    defaultValue = 0


_WmanIfBsSsMaxNumOfClassifier_Type.__name__ = "Integer32"
_WmanIfBsSsMaxNumOfClassifier_Object = MibTableColumn
wmanIfBsSsMaxNumOfClassifier = _WmanIfBsSsMaxNumOfClassifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 19),
    _WmanIfBsSsMaxNumOfClassifier_Type()
)
wmanIfBsSsMaxNumOfClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsMaxNumOfClassifier.setStatus("current")


class _WmanIfBsSsPhsSupport_Type(Integer32):
    """Custom type wmanIfBsSsPhsSupport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhsSupport", 0),
          ("atmPhsSupport", 1),
          ("packetPhsSupport", 2))
    )


_WmanIfBsSsPhsSupport_Type.__name__ = "Integer32"
_WmanIfBsSsPhsSupport_Object = MibTableColumn
wmanIfBsSsPhsSupport = _WmanIfBsSsPhsSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 20),
    _WmanIfBsSsPhsSupport_Type()
)
wmanIfBsSsPhsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsPhsSupport.setStatus("current")


class _WmanIfBsSsIpManagementSupport_Type(Integer32):
    """Custom type wmanIfBsSsIpManagementSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmanaged", 0),
          ("ipManaged", 1))
    )


_WmanIfBsSsIpManagementSupport_Type.__name__ = "Integer32"
_WmanIfBsSsIpManagementSupport_Object = MibTableColumn
wmanIfBsSsIpManagementSupport = _WmanIfBsSsIpManagementSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 21),
    _WmanIfBsSsIpManagementSupport_Type()
)
wmanIfBsSsIpManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsIpManagementSupport.setStatus("current")
_WmanIfBsSs2ndMgmtArqEnable_Type = TruthValue
_WmanIfBsSs2ndMgmtArqEnable_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqEnable = _WmanIfBsSs2ndMgmtArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 22),
    _WmanIfBsSs2ndMgmtArqEnable_Type()
)
wmanIfBsSs2ndMgmtArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqEnable.setStatus("current")


class _WmanIfBsSs2ndMgmtArqWindowSize_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfBsSs2ndMgmtArqWindowSize_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqWindowSize_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqWindowSize = _WmanIfBsSs2ndMgmtArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 23),
    _WmanIfBsSs2ndMgmtArqWindowSize_Type()
)
wmanIfBsSs2ndMgmtArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqWindowSize.setStatus("current")


class _WmanIfBsSs2ndMgmtArqFragmentLifetime_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqFragmentLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqFragmentLifetime_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqFragmentLifetime_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqFragmentLifetime = _WmanIfBsSs2ndMgmtArqFragmentLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 24),
    _WmanIfBsSs2ndMgmtArqFragmentLifetime_Type()
)
wmanIfBsSs2ndMgmtArqFragmentLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqFragmentLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqFragmentLifetime.setUnits("10 us")


class _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqSyncLossTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqSyncLossTimeout_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqSyncLossTimeout = _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 25),
    _WmanIfBsSs2ndMgmtArqSyncLossTimeout_Type()
)
wmanIfBsSs2ndMgmtArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqSyncLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqSyncLossTimeout.setUnits("10 us")
_WmanIfBsSs2ndMgmtArqDeliverInOrder_Type = TruthValue
_WmanIfBsSs2ndMgmtArqDeliverInOrder_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqDeliverInOrder = _WmanIfBsSs2ndMgmtArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 26),
    _WmanIfBsSs2ndMgmtArqDeliverInOrder_Type()
)
wmanIfBsSs2ndMgmtArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqDeliverInOrder.setStatus("current")


class _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfBsSs2ndMgmtArqRxPurgeTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Object = MibTableColumn
wmanIfBsSs2ndMgmtArqRxPurgeTimeout = _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 27),
    _WmanIfBsSs2ndMgmtArqRxPurgeTimeout_Type()
)
wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSs2ndMgmtArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfBsSsVendorIdEncoding_Type(OctetString):
    """Custom type wmanIfBsSsVendorIdEncoding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_WmanIfBsSsVendorIdEncoding_Type.__name__ = "OctetString"
_WmanIfBsSsVendorIdEncoding_Object = MibTableColumn
wmanIfBsSsVendorIdEncoding = _WmanIfBsSsVendorIdEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 1, 1, 28),
    _WmanIfBsSsVendorIdEncoding_Type()
)
wmanIfBsSsVendorIdEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsVendorIdEncoding.setStatus("current")
_WmanIfBsConfigurationTable_Object = MibTable
wmanIfBsConfigurationTable = _WmanIfBsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsConfigurationTable.setStatus("current")
_WmanIfBsConfigurationEntry_Object = MibTableRow
wmanIfBsConfigurationEntry = _WmanIfBsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1)
)
wmanIfBsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsConfigurationEntry.setStatus("current")


class _WmanIfBsDcdInterval_Type(Integer32):
    """Custom type wmanIfBsDcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfBsDcdInterval_Type.__name__ = "Integer32"
_WmanIfBsDcdInterval_Object = MibTableColumn
wmanIfBsDcdInterval = _WmanIfBsDcdInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 1),
    _WmanIfBsDcdInterval_Type()
)
wmanIfBsDcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsDcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsDcdInterval.setUnits("milliseconds")


class _WmanIfBsUcdInterval_Type(Integer32):
    """Custom type wmanIfBsUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfBsUcdInterval_Type.__name__ = "Integer32"
_WmanIfBsUcdInterval_Object = MibTableColumn
wmanIfBsUcdInterval = _WmanIfBsUcdInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 2),
    _WmanIfBsUcdInterval_Type()
)
wmanIfBsUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsUcdInterval.setUnits("milliseconds")
_WmanIfBsUcdTransition_Type = Integer32
_WmanIfBsUcdTransition_Object = MibTableColumn
wmanIfBsUcdTransition = _WmanIfBsUcdTransition_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 3),
    _WmanIfBsUcdTransition_Type()
)
wmanIfBsUcdTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsUcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsUcdTransition.setUnits("Number of MAC Frames")
_WmanIfBsDcdTransition_Type = Integer32
_WmanIfBsDcdTransition_Object = MibTableColumn
wmanIfBsDcdTransition = _WmanIfBsDcdTransition_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 4),
    _WmanIfBsDcdTransition_Type()
)
wmanIfBsDcdTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsDcdTransition.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsDcdTransition.setUnits("Number of MAC Frames")
_WmanIfBsMaxMAPPending_Type = Integer32
_WmanIfBsMaxMAPPending_Object = MibTableColumn
wmanIfBsMaxMAPPending = _WmanIfBsMaxMAPPending_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 5),
    _WmanIfBsMaxMAPPending_Type()
)
wmanIfBsMaxMAPPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsMaxMAPPending.setStatus("current")


class _WmanIfBsInitialRangingInterval_Type(Integer32):
    """Custom type wmanIfBsInitialRangingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_WmanIfBsInitialRangingInterval_Type.__name__ = "Integer32"
_WmanIfBsInitialRangingInterval_Object = MibTableColumn
wmanIfBsInitialRangingInterval = _WmanIfBsInitialRangingInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 6),
    _WmanIfBsInitialRangingInterval_Type()
)
wmanIfBsInitialRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsInitialRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsInitialRangingInterval.setUnits("milliseconds")


class _WmanIfBsClkCmpInterval_Type(Integer32):
    """Custom type wmanIfBsClkCmpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50),
    )


_WmanIfBsClkCmpInterval_Type.__name__ = "Integer32"
_WmanIfBsClkCmpInterval_Object = MibTableColumn
wmanIfBsClkCmpInterval = _WmanIfBsClkCmpInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 7),
    _WmanIfBsClkCmpInterval_Type()
)
wmanIfBsClkCmpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsClkCmpInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsClkCmpInterval.setUnits("milliseconds")


class _WmanIfBsSsULMapProcTime_Type(Unsigned32):
    """Custom type wmanIfBsSsULMapProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4294967295),
    )


_WmanIfBsSsULMapProcTime_Type.__name__ = "Unsigned32"
_WmanIfBsSsULMapProcTime_Object = MibTableColumn
wmanIfBsSsULMapProcTime = _WmanIfBsSsULMapProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 8),
    _WmanIfBsSsULMapProcTime_Type()
)
wmanIfBsSsULMapProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsULMapProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsULMapProcTime.setUnits("micro seconds")


class _WmanIfBsSsRangRespProcTime_Type(Unsigned32):
    """Custom type wmanIfBsSsRangRespProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_WmanIfBsSsRangRespProcTime_Type.__name__ = "Unsigned32"
_WmanIfBsSsRangRespProcTime_Object = MibTableColumn
wmanIfBsSsRangRespProcTime = _WmanIfBsSsRangRespProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 9),
    _WmanIfBsSsRangRespProcTime_Type()
)
wmanIfBsSsRangRespProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsSsRangRespProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsSsRangRespProcTime.setUnits("micro seconds")


class _WmanIfBsT5Timeout_Type(Integer32):
    """Custom type wmanIfBsT5Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_WmanIfBsT5Timeout_Type.__name__ = "Integer32"
_WmanIfBsT5Timeout_Object = MibTableColumn
wmanIfBsT5Timeout = _WmanIfBsT5Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 10),
    _WmanIfBsT5Timeout_Type()
)
wmanIfBsT5Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT5Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT5Timeout.setUnits("milliseconds")


class _WmanIfBsT9Timeout_Type(Integer32):
    """Custom type wmanIfBsT9Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 65535),
    )


_WmanIfBsT9Timeout_Type.__name__ = "Integer32"
_WmanIfBsT9Timeout_Object = MibTableColumn
wmanIfBsT9Timeout = _WmanIfBsT9Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 11),
    _WmanIfBsT9Timeout_Type()
)
wmanIfBsT9Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT9Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT9Timeout.setUnits("milliseconds")


class _WmanIfBsT13Timeout_Type(Integer32):
    """Custom type wmanIfBsT13Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_WmanIfBsT13Timeout_Type.__name__ = "Integer32"
_WmanIfBsT13Timeout_Object = MibTableColumn
wmanIfBsT13Timeout = _WmanIfBsT13Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 12),
    _WmanIfBsT13Timeout_Type()
)
wmanIfBsT13Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT13Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT13Timeout.setUnits("minutes")


class _WmanIfBsT15Timeout_Type(Integer32):
    """Custom type wmanIfBsT15Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 65535),
    )


_WmanIfBsT15Timeout_Type.__name__ = "Integer32"
_WmanIfBsT15Timeout_Object = MibTableColumn
wmanIfBsT15Timeout = _WmanIfBsT15Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 13),
    _WmanIfBsT15Timeout_Type()
)
wmanIfBsT15Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT15Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT15Timeout.setUnits("milliseconds")


class _WmanIfBsT17Timeout_Type(Integer32):
    """Custom type wmanIfBsT17Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WmanIfBsT17Timeout_Type.__name__ = "Integer32"
_WmanIfBsT17Timeout_Object = MibTableColumn
wmanIfBsT17Timeout = _WmanIfBsT17Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 14),
    _WmanIfBsT17Timeout_Type()
)
wmanIfBsT17Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT17Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT17Timeout.setUnits("minutes")
_WmanIfBsT27IdleTimer_Type = Integer32
_WmanIfBsT27IdleTimer_Object = MibTableColumn
wmanIfBsT27IdleTimer = _WmanIfBsT27IdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 15),
    _WmanIfBsT27IdleTimer_Type()
)
wmanIfBsT27IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT27IdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT27IdleTimer.setUnits("milliseconds")
_WmanIfBsT27ActiveTimer_Type = Integer32
_WmanIfBsT27ActiveTimer_Object = MibTableColumn
wmanIfBsT27ActiveTimer = _WmanIfBsT27ActiveTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 2, 1, 16),
    _WmanIfBsT27ActiveTimer_Type()
)
wmanIfBsT27ActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsT27ActiveTimer.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsT27ActiveTimer.setUnits("milliseconds")
_WmanIfBsStatisticCounter_ObjectIdentity = ObjectIdentity
wmanIfBsStatisticCounter = _WmanIfBsStatisticCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3)
)
_WmanIfBsChMeasurementTable_Object = MibTable
wmanIfBsChMeasurementTable = _WmanIfBsChMeasurementTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsChMeasurementTable.setStatus("deprecated")
_WmanIfBsChMeasurementEntry_Object = MibTableRow
wmanIfBsChMeasurementEntry = _WmanIfBsChMeasurementEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1)
)
wmanIfBsChMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsChSsIdIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsChMeasurementEntry.setStatus("deprecated")


class _WmanIfBsChSsIdIndex_Type(Unsigned32):
    """Custom type wmanIfBsChSsIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsChSsIdIndex_Type.__name__ = "Unsigned32"
_WmanIfBsChSsIdIndex_Object = MibTableColumn
wmanIfBsChSsIdIndex = _WmanIfBsChSsIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 1),
    _WmanIfBsChSsIdIndex_Type()
)
wmanIfBsChSsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsChSsIdIndex.setStatus("deprecated")


class _WmanIfBsHistogramIndex_Type(Unsigned32):
    """Custom type wmanIfBsHistogramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsHistogramIndex_Type.__name__ = "Unsigned32"
_WmanIfBsHistogramIndex_Object = MibTableColumn
wmanIfBsHistogramIndex = _WmanIfBsHistogramIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 2),
    _WmanIfBsHistogramIndex_Type()
)
wmanIfBsHistogramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsHistogramIndex.setStatus("deprecated")
_WmanIfBsChannelNumber_Type = Integer32
_WmanIfBsChannelNumber_Object = MibTableColumn
wmanIfBsChannelNumber = _WmanIfBsChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 3),
    _WmanIfBsChannelNumber_Type()
)
wmanIfBsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsChannelNumber.setStatus("deprecated")
_WmanIfBsStartFrame_Type = Integer32
_WmanIfBsStartFrame_Object = MibTableColumn
wmanIfBsStartFrame = _WmanIfBsStartFrame_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 4),
    _WmanIfBsStartFrame_Type()
)
wmanIfBsStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStartFrame.setStatus("deprecated")
_WmanIfBsDuration_Type = Integer32
_WmanIfBsDuration_Object = MibTableColumn
wmanIfBsDuration = _WmanIfBsDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 5),
    _WmanIfBsDuration_Type()
)
wmanIfBsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDuration.setStatus("deprecated")


class _WmanIfBsBasicReport_Type(Bits):
    """Custom type wmanIfBsBasicReport based on Bits"""
    namedValues = NamedValues(
        *(("wirelessHuman", 0),
          ("unknownTransmission", 1),
          ("primaryUser", 2),
          ("channegNotMeasured", 3))
    )

_WmanIfBsBasicReport_Type.__name__ = "Bits"
_WmanIfBsBasicReport_Object = MibTableColumn
wmanIfBsBasicReport = _WmanIfBsBasicReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 6),
    _WmanIfBsBasicReport_Type()
)
wmanIfBsBasicReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsBasicReport.setStatus("deprecated")
_WmanIfBsMeanCinrReport_Type = Integer32
_WmanIfBsMeanCinrReport_Object = MibTableColumn
wmanIfBsMeanCinrReport = _WmanIfBsMeanCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 7),
    _WmanIfBsMeanCinrReport_Type()
)
wmanIfBsMeanCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsMeanCinrReport.setStatus("deprecated")
_WmanIfBsMeanRssiReport_Type = Integer32
_WmanIfBsMeanRssiReport_Object = MibTableColumn
wmanIfBsMeanRssiReport = _WmanIfBsMeanRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 8),
    _WmanIfBsMeanRssiReport_Type()
)
wmanIfBsMeanRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsMeanRssiReport.setStatus("deprecated")
_WmanIfBsStdDeviationCinrReport_Type = Integer32
_WmanIfBsStdDeviationCinrReport_Object = MibTableColumn
wmanIfBsStdDeviationCinrReport = _WmanIfBsStdDeviationCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 9),
    _WmanIfBsStdDeviationCinrReport_Type()
)
wmanIfBsStdDeviationCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationCinrReport.setStatus("deprecated")
_WmanIfBsStdDeviationRssiReport_Type = Integer32
_WmanIfBsStdDeviationRssiReport_Object = MibTableColumn
wmanIfBsStdDeviationRssiReport = _WmanIfBsStdDeviationRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 1, 1, 10),
    _WmanIfBsStdDeviationRssiReport_Type()
)
wmanIfBsStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsStdDeviationRssiReport.setStatus("deprecated")
_WmanIfBsFecCounterTable_Object = MibTable
wmanIfBsFecCounterTable = _WmanIfBsFecCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsFecCounterTable.setStatus("current")
_WmanIfBsFecCounterEntry_Object = MibTableRow
wmanIfBsFecCounterEntry = _WmanIfBsFecCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1)
)
wmanIfBsFecCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsFecSsId"),
)
if mibBuilder.loadTexts:
    wmanIfBsFecCounterEntry.setStatus("current")


class _WmanIfBsFecSsId_Type(Unsigned32):
    """Custom type wmanIfBsFecSsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsFecSsId_Type.__name__ = "Unsigned32"
_WmanIfBsFecSsId_Object = MibTableColumn
wmanIfBsFecSsId = _WmanIfBsFecSsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1, 1),
    _WmanIfBsFecSsId_Type()
)
wmanIfBsFecSsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsFecSsId.setStatus("current")
_WmanIfBsFecCorrectedBytes_Type = Counter64
_WmanIfBsFecCorrectedBytes_Object = MibTableColumn
wmanIfBsFecCorrectedBytes = _WmanIfBsFecCorrectedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1, 2),
    _WmanIfBsFecCorrectedBytes_Type()
)
wmanIfBsFecCorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsFecCorrectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsFecCorrectedBytes.setUnits("bytes")
_WmanIfBsFecUncorrectedBytes_Type = Counter64
_WmanIfBsFecUncorrectedBytes_Object = MibTableColumn
wmanIfBsFecUncorrectedBytes = _WmanIfBsFecUncorrectedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1, 3),
    _WmanIfBsFecUncorrectedBytes_Type()
)
wmanIfBsFecUncorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsFecUncorrectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsFecUncorrectedBytes.setUnits("bytes")
_WmanIfBsFecUncorrectedMacPdu_Type = Counter64
_WmanIfBsFecUncorrectedMacPdu_Object = MibTableColumn
wmanIfBsFecUncorrectedMacPdu = _WmanIfBsFecUncorrectedMacPdu_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1, 4),
    _WmanIfBsFecUncorrectedMacPdu_Type()
)
wmanIfBsFecUncorrectedMacPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsFecUncorrectedMacPdu.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsFecUncorrectedMacPdu.setUnits("MAC PDU")


class _WmanIfBsFecResetCounter_Type(Integer32):
    """Custom type wmanIfBsFecResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("resetCounter", 1))
    )


_WmanIfBsFecResetCounter_Type.__name__ = "Integer32"
_WmanIfBsFecResetCounter_Object = MibTableColumn
wmanIfBsFecResetCounter = _WmanIfBsFecResetCounter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 2, 3, 2, 1, 5),
    _WmanIfBsFecResetCounter_Type()
)
wmanIfBsFecResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsFecResetCounter.setStatus("current")
_WmanIfBsPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfBsPkmObjects = _WmanIfBsPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3)
)
_WmanIfBsPkmBaseTable_Object = MibTable
wmanIfBsPkmBaseTable = _WmanIfBsPkmBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsPkmBaseTable.setStatus("current")
_WmanIfBsPkmBaseEntry_Object = MibTableRow
wmanIfBsPkmBaseEntry = _WmanIfBsPkmBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1)
)
wmanIfBsPkmBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsPkmBaseEntry.setStatus("current")


class _WmanIfBsPkmDefaultAuthLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultAuthLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIfBsPkmDefaultAuthLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultAuthLifetime_Object = MibTableColumn
wmanIfBsPkmDefaultAuthLifetime = _WmanIfBsPkmDefaultAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 1),
    _WmanIfBsPkmDefaultAuthLifetime_Type()
)
wmanIfBsPkmDefaultAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultAuthLifetime.setUnits("seconds")


class _WmanIfBsPkmDefaultTEKLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultTEKLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIfBsPkmDefaultTEKLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultTEKLifetime_Object = MibTableColumn
wmanIfBsPkmDefaultTEKLifetime = _WmanIfBsPkmDefaultTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 2),
    _WmanIfBsPkmDefaultTEKLifetime_Type()
)
wmanIfBsPkmDefaultTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultTEKLifetime.setUnits("seconds")


class _WmanIfBsPkmDefaultSelfSigManufCertTrust_Type(Integer32):
    """Custom type wmanIfBsPkmDefaultSelfSigManufCertTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_WmanIfBsPkmDefaultSelfSigManufCertTrust_Type.__name__ = "Integer32"
_WmanIfBsPkmDefaultSelfSigManufCertTrust_Object = MibTableColumn
wmanIfBsPkmDefaultSelfSigManufCertTrust = _WmanIfBsPkmDefaultSelfSigManufCertTrust_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 3),
    _WmanIfBsPkmDefaultSelfSigManufCertTrust_Type()
)
wmanIfBsPkmDefaultSelfSigManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmDefaultSelfSigManufCertTrust.setStatus("current")
_WmanIfBsPkmCheckCertValidityPeriods_Type = TruthValue
_WmanIfBsPkmCheckCertValidityPeriods_Object = MibTableColumn
wmanIfBsPkmCheckCertValidityPeriods = _WmanIfBsPkmCheckCertValidityPeriods_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 4),
    _WmanIfBsPkmCheckCertValidityPeriods_Type()
)
wmanIfBsPkmCheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmCheckCertValidityPeriods.setStatus("current")
_WmanIfBsPkmAuthentInfos_Type = Counter32
_WmanIfBsPkmAuthentInfos_Object = MibTableColumn
wmanIfBsPkmAuthentInfos = _WmanIfBsPkmAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 5),
    _WmanIfBsPkmAuthentInfos_Type()
)
wmanIfBsPkmAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthentInfos.setStatus("current")
_WmanIfBsPkmAuthRequests_Type = Counter32
_WmanIfBsPkmAuthRequests_Object = MibTableColumn
wmanIfBsPkmAuthRequests = _WmanIfBsPkmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 6),
    _WmanIfBsPkmAuthRequests_Type()
)
wmanIfBsPkmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRequests.setStatus("current")
_WmanIfBsPkmAuthReplies_Type = Counter32
_WmanIfBsPkmAuthReplies_Object = MibTableColumn
wmanIfBsPkmAuthReplies = _WmanIfBsPkmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 7),
    _WmanIfBsPkmAuthReplies_Type()
)
wmanIfBsPkmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthReplies.setStatus("current")
_WmanIfBsPkmAuthRejects_Type = Counter32
_WmanIfBsPkmAuthRejects_Object = MibTableColumn
wmanIfBsPkmAuthRejects = _WmanIfBsPkmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 8),
    _WmanIfBsPkmAuthRejects_Type()
)
wmanIfBsPkmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRejects.setStatus("current")
_WmanIfBsPkmAuthInvalids_Type = Counter32
_WmanIfBsPkmAuthInvalids_Object = MibTableColumn
wmanIfBsPkmAuthInvalids = _WmanIfBsPkmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 1, 1, 9),
    _WmanIfBsPkmAuthInvalids_Type()
)
wmanIfBsPkmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthInvalids.setStatus("current")
_WmanIfBsPkmAuthTable_Object = MibTable
wmanIfBsPkmAuthTable = _WmanIfBsPkmAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthTable.setStatus("current")
_WmanIfBsPkmAuthEntry_Object = MibTableRow
wmanIfBsPkmAuthEntry = _WmanIfBsPkmAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1)
)
wmanIfBsPkmAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsPkmAuthSsMacAddress"),
)
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthEntry.setStatus("current")
_WmanIfBsPkmAuthSsMacAddress_Type = VariableMacAddress
_WmanIfBsPkmAuthSsMacAddress_Object = MibTableColumn
wmanIfBsPkmAuthSsMacAddress = _WmanIfBsPkmAuthSsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 1),
    _WmanIfBsPkmAuthSsMacAddress_Type()
)
wmanIfBsPkmAuthSsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsMacAddress.setStatus("current")


class _WmanIfBsPkmAuthSsPublicKey_Type(OctetString):
    """Custom type wmanIfBsPkmAuthSsPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(140, 140),
    )
    fixedLength = 140


_WmanIfBsPkmAuthSsPublicKey_Type.__name__ = "OctetString"
_WmanIfBsPkmAuthSsPublicKey_Object = MibTableColumn
wmanIfBsPkmAuthSsPublicKey = _WmanIfBsPkmAuthSsPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 2),
    _WmanIfBsPkmAuthSsPublicKey_Type()
)
wmanIfBsPkmAuthSsPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsPublicKey.setStatus("current")


class _WmanIfBsPkmAuthSsKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfBsPkmAuthSsKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfBsPkmAuthSsKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthSsKeySequenceNumber_Object = MibTableColumn
wmanIfBsPkmAuthSsKeySequenceNumber = _WmanIfBsPkmAuthSsKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 3),
    _WmanIfBsPkmAuthSsKeySequenceNumber_Type()
)
wmanIfBsPkmAuthSsKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsKeySequenceNumber.setStatus("current")
_WmanIfBsPkmAuthSsExpiresOld_Type = DateAndTime
_WmanIfBsPkmAuthSsExpiresOld_Object = MibTableColumn
wmanIfBsPkmAuthSsExpiresOld = _WmanIfBsPkmAuthSsExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 4),
    _WmanIfBsPkmAuthSsExpiresOld_Type()
)
wmanIfBsPkmAuthSsExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsExpiresOld.setStatus("current")
_WmanIfBsPkmAuthSsExpiresNew_Type = DateAndTime
_WmanIfBsPkmAuthSsExpiresNew_Object = MibTableColumn
wmanIfBsPkmAuthSsExpiresNew = _WmanIfBsPkmAuthSsExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 5),
    _WmanIfBsPkmAuthSsExpiresNew_Type()
)
wmanIfBsPkmAuthSsExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsExpiresNew.setStatus("current")


class _WmanIfBsPkmAuthSsLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmAuthSsLifetime based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 6048000),
    )


_WmanIfBsPkmAuthSsLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthSsLifetime_Object = MibTableColumn
wmanIfBsPkmAuthSsLifetime = _WmanIfBsPkmAuthSsLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 6),
    _WmanIfBsPkmAuthSsLifetime_Type()
)
wmanIfBsPkmAuthSsLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsLifetime.setUnits("seconds")


class _WmanIfBsPkmAuthSsReset_Type(Integer32):
    """Custom type wmanIfBsPkmAuthSsReset based on Integer32"""
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
        *(("noResetRequested", 1),
          ("invalidateAuth", 2),
          ("sendAuthInvalid", 3),
          ("invalidateTeks", 4))
    )


_WmanIfBsPkmAuthSsReset_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthSsReset_Object = MibTableColumn
wmanIfBsPkmAuthSsReset = _WmanIfBsPkmAuthSsReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 7),
    _WmanIfBsPkmAuthSsReset_Type()
)
wmanIfBsPkmAuthSsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsReset.setStatus("current")
_WmanIfBsPkmAuthSsInfos_Type = Counter64
_WmanIfBsPkmAuthSsInfos_Object = MibTableColumn
wmanIfBsPkmAuthSsInfos = _WmanIfBsPkmAuthSsInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 8),
    _WmanIfBsPkmAuthSsInfos_Type()
)
wmanIfBsPkmAuthSsInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsInfos.setStatus("current")
_WmanIfBsPkmAuthSsRequests_Type = Counter64
_WmanIfBsPkmAuthSsRequests_Object = MibTableColumn
wmanIfBsPkmAuthSsRequests = _WmanIfBsPkmAuthSsRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 9),
    _WmanIfBsPkmAuthSsRequests_Type()
)
wmanIfBsPkmAuthSsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsRequests.setStatus("current")
_WmanIfBsPkmAuthSsReplies_Type = Counter64
_WmanIfBsPkmAuthSsReplies_Object = MibTableColumn
wmanIfBsPkmAuthSsReplies = _WmanIfBsPkmAuthSsReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 10),
    _WmanIfBsPkmAuthSsReplies_Type()
)
wmanIfBsPkmAuthSsReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsReplies.setStatus("current")
_WmanIfBsPkmAuthSsRejects_Type = Counter64
_WmanIfBsPkmAuthSsRejects_Object = MibTableColumn
wmanIfBsPkmAuthSsRejects = _WmanIfBsPkmAuthSsRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 11),
    _WmanIfBsPkmAuthSsRejects_Type()
)
wmanIfBsPkmAuthSsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsRejects.setStatus("current")
_WmanIfBsPkmAuthSsInvalids_Type = Counter64
_WmanIfBsPkmAuthSsInvalids_Object = MibTableColumn
wmanIfBsPkmAuthSsInvalids = _WmanIfBsPkmAuthSsInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 12),
    _WmanIfBsPkmAuthSsInvalids_Type()
)
wmanIfBsPkmAuthSsInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthSsInvalids.setStatus("current")


class _WmanIfBsPkmAuthRejectErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSs", 1),
          ("unauthorizedSaid", 2),
          ("permanentAuthorizationFailure", 6))
    )


_WmanIfBsPkmAuthRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthRejectErrorCode_Object = MibTableColumn
wmanIfBsPkmAuthRejectErrorCode = _WmanIfBsPkmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 13),
    _WmanIfBsPkmAuthRejectErrorCode_Type()
)
wmanIfBsPkmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRejectErrorCode.setStatus("current")


class _WmanIfBsPkmAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmAuthRejectErrorString_Object = MibTableColumn
wmanIfBsPkmAuthRejectErrorString = _WmanIfBsPkmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 14),
    _WmanIfBsPkmAuthRejectErrorString_Type()
)
wmanIfBsPkmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthRejectErrorString.setStatus("current")


class _WmanIfBsPkmAuthInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSs", 1),
          ("unsolicited", 3),
          ("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5))
    )


_WmanIfBsPkmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthInvalidErrorCode_Object = MibTableColumn
wmanIfBsPkmAuthInvalidErrorCode = _WmanIfBsPkmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 15),
    _WmanIfBsPkmAuthInvalidErrorCode_Type()
)
wmanIfBsPkmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthInvalidErrorCode.setStatus("current")


class _WmanIfBsPkmAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmAuthInvalidErrorString_Object = MibTableColumn
wmanIfBsPkmAuthInvalidErrorString = _WmanIfBsPkmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 16),
    _WmanIfBsPkmAuthInvalidErrorString_Type()
)
wmanIfBsPkmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthInvalidErrorString.setStatus("current")


class _WmanIfBsPkmAuthPrimarySAId_Type(Integer32):
    """Custom type wmanIfBsPkmAuthPrimarySAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WmanIfBsPkmAuthPrimarySAId_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthPrimarySAId_Object = MibTableColumn
wmanIfBsPkmAuthPrimarySAId = _WmanIfBsPkmAuthPrimarySAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 17),
    _WmanIfBsPkmAuthPrimarySAId_Type()
)
wmanIfBsPkmAuthPrimarySAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthPrimarySAId.setStatus("current")


class _WmanIfBsPkmAuthBpkmSsCertValid_Type(Integer32):
    """Custom type wmanIfBsPkmAuthBpkmSsCertValid based on Integer32"""
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
        *(("unknown", 0),
          ("validSsChained", 1),
          ("validSsTrusted", 2),
          ("invalidSsUntrusted", 3),
          ("invalidCAUntrusted", 4),
          ("invalidSsOther", 5),
          ("invalidCAOther", 6))
    )


_WmanIfBsPkmAuthBpkmSsCertValid_Type.__name__ = "Integer32"
_WmanIfBsPkmAuthBpkmSsCertValid_Object = MibTableColumn
wmanIfBsPkmAuthBpkmSsCertValid = _WmanIfBsPkmAuthBpkmSsCertValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 18),
    _WmanIfBsPkmAuthBpkmSsCertValid_Type()
)
wmanIfBsPkmAuthBpkmSsCertValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthBpkmSsCertValid.setStatus("current")
_WmanIfBsPkmAuthBpkmSsCert_Type = OctetString
_WmanIfBsPkmAuthBpkmSsCert_Object = MibTableColumn
wmanIfBsPkmAuthBpkmSsCert = _WmanIfBsPkmAuthBpkmSsCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 2, 1, 19),
    _WmanIfBsPkmAuthBpkmSsCert_Type()
)
wmanIfBsPkmAuthBpkmSsCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmAuthBpkmSsCert.setStatus("current")
_WmanIfBsPkmTEKTable_Object = MibTable
wmanIfBsPkmTEKTable = _WmanIfBsPkmTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKTable.setStatus("current")
_WmanIfBsPkmTEKEntry_Object = MibTableRow
wmanIfBsPkmTEKEntry = _WmanIfBsPkmTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1)
)
wmanIfBsPkmTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsPkmTEKSAId"),
)
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKEntry.setStatus("current")


class _WmanIfBsPkmTEKSAId_Type(Integer32):
    """Custom type wmanIfBsPkmTEKSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WmanIfBsPkmTEKSAId_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKSAId_Object = MibTableColumn
wmanIfBsPkmTEKSAId = _WmanIfBsPkmTEKSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 1),
    _WmanIfBsPkmTEKSAId_Type()
)
wmanIfBsPkmTEKSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKSAId.setStatus("current")


class _WmanIfBsPkmTEKSAType_Type(Integer32):
    """Custom type wmanIfBsPkmTEKSAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySA", 0),
          ("staticSA", 1),
          ("dynamicSA", 2))
    )


_WmanIfBsPkmTEKSAType_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKSAType_Object = MibTableColumn
wmanIfBsPkmTEKSAType = _WmanIfBsPkmTEKSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 2),
    _WmanIfBsPkmTEKSAType_Type()
)
wmanIfBsPkmTEKSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKSAType.setStatus("current")


class _WmanIfBsPkmTEKDataEncryptAlg_Type(Integer32):
    """Custom type wmanIfBsPkmTEKDataEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des56CbcMode", 1))
    )


_WmanIfBsPkmTEKDataEncryptAlg_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKDataEncryptAlg_Object = MibTableColumn
wmanIfBsPkmTEKDataEncryptAlg = _WmanIfBsPkmTEKDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 3),
    _WmanIfBsPkmTEKDataEncryptAlg_Type()
)
wmanIfBsPkmTEKDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKDataEncryptAlg.setStatus("current")


class _WmanIfBsPkmTEKDataAuthentAlg_Type(Integer32):
    """Custom type wmanIfBsPkmTEKDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_WmanIfBsPkmTEKDataAuthentAlg_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKDataAuthentAlg_Object = MibTableColumn
wmanIfBsPkmTEKDataAuthentAlg = _WmanIfBsPkmTEKDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 4),
    _WmanIfBsPkmTEKDataAuthentAlg_Type()
)
wmanIfBsPkmTEKDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKDataAuthentAlg.setStatus("current")


class _WmanIfBsPkmTEKEncryptAlg_Type(Integer32):
    """Custom type wmanIfBsPkmTEKEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tripleDES", 0),
          ("rsa1024", 1))
    )


_WmanIfBsPkmTEKEncryptAlg_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKEncryptAlg_Object = MibTableColumn
wmanIfBsPkmTEKEncryptAlg = _WmanIfBsPkmTEKEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 5),
    _WmanIfBsPkmTEKEncryptAlg_Type()
)
wmanIfBsPkmTEKEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKEncryptAlg.setStatus("current")


class _WmanIfBsPkmTEKLifetime_Type(Integer32):
    """Custom type wmanIfBsPkmTEKLifetime based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 604800),
    )


_WmanIfBsPkmTEKLifetime_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKLifetime_Object = MibTableColumn
wmanIfBsPkmTEKLifetime = _WmanIfBsPkmTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 6),
    _WmanIfBsPkmTEKLifetime_Type()
)
wmanIfBsPkmTEKLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKLifetime.setUnits("seconds")


class _WmanIfBsPkmTEKKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfBsPkmTEKKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIfBsPkmTEKKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKKeySequenceNumber_Object = MibTableColumn
wmanIfBsPkmTEKKeySequenceNumber = _WmanIfBsPkmTEKKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 7),
    _WmanIfBsPkmTEKKeySequenceNumber_Type()
)
wmanIfBsPkmTEKKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKKeySequenceNumber.setStatus("current")
_WmanIfBsPkmTEKExpiresOld_Type = DateAndTime
_WmanIfBsPkmTEKExpiresOld_Object = MibTableColumn
wmanIfBsPkmTEKExpiresOld = _WmanIfBsPkmTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 8),
    _WmanIfBsPkmTEKExpiresOld_Type()
)
wmanIfBsPkmTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKExpiresOld.setStatus("current")
_WmanIfBsPkmTEKExpiresNew_Type = DateAndTime
_WmanIfBsPkmTEKExpiresNew_Object = MibTableColumn
wmanIfBsPkmTEKExpiresNew = _WmanIfBsPkmTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 9),
    _WmanIfBsPkmTEKExpiresNew_Type()
)
wmanIfBsPkmTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKExpiresNew.setStatus("current")
_WmanIfBsPkmTEKReset_Type = TruthValue
_WmanIfBsPkmTEKReset_Object = MibTableColumn
wmanIfBsPkmTEKReset = _WmanIfBsPkmTEKReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 10),
    _WmanIfBsPkmTEKReset_Type()
)
wmanIfBsPkmTEKReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKReset.setStatus("current")
_WmanIfBsPkmKeyRequests_Type = Counter32
_WmanIfBsPkmKeyRequests_Object = MibTableColumn
wmanIfBsPkmKeyRequests = _WmanIfBsPkmKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 11),
    _WmanIfBsPkmKeyRequests_Type()
)
wmanIfBsPkmKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRequests.setStatus("current")
_WmanIfBsPkmKeyReplies_Type = Counter32
_WmanIfBsPkmKeyReplies_Object = MibTableColumn
wmanIfBsPkmKeyReplies = _WmanIfBsPkmKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 12),
    _WmanIfBsPkmKeyReplies_Type()
)
wmanIfBsPkmKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyReplies.setStatus("current")
_WmanIfBsPkmKeyRejects_Type = Counter32
_WmanIfBsPkmKeyRejects_Object = MibTableColumn
wmanIfBsPkmKeyRejects = _WmanIfBsPkmKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 13),
    _WmanIfBsPkmKeyRejects_Type()
)
wmanIfBsPkmKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejects.setStatus("current")
_WmanIfBsPkmTEKInvalids_Type = Counter32
_WmanIfBsPkmTEKInvalids_Object = MibTableColumn
wmanIfBsPkmTEKInvalids = _WmanIfBsPkmTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 14),
    _WmanIfBsPkmTEKInvalids_Type()
)
wmanIfBsPkmTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKInvalids.setStatus("current")


class _WmanIfBsPkmKeyRejectErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("unauthorizedSaid", 2))
    )


_WmanIfBsPkmKeyRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmKeyRejectErrorCode_Object = MibTableColumn
wmanIfBsPkmKeyRejectErrorCode = _WmanIfBsPkmKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 15),
    _WmanIfBsPkmKeyRejectErrorCode_Type()
)
wmanIfBsPkmKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejectErrorCode.setStatus("current")


class _WmanIfBsPkmKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmKeyRejectErrorString_Object = MibTableColumn
wmanIfBsPkmKeyRejectErrorString = _WmanIfBsPkmKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 16),
    _WmanIfBsPkmKeyRejectErrorString_Type()
)
wmanIfBsPkmKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmKeyRejectErrorString.setStatus("current")


class _WmanIfBsPkmTEKInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfBsPkmTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noInformation", 0),
          ("invalidKeySequence", 4))
    )


_WmanIfBsPkmTEKInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfBsPkmTEKInvalidErrorCode_Object = MibTableColumn
wmanIfBsPkmTEKInvalidErrorCode = _WmanIfBsPkmTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 17),
    _WmanIfBsPkmTEKInvalidErrorCode_Type()
)
wmanIfBsPkmTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKInvalidErrorCode.setStatus("current")


class _WmanIfBsPkmTEKInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfBsPkmTEKInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfBsPkmTEKInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfBsPkmTEKInvalidErrorString_Object = MibTableColumn
wmanIfBsPkmTEKInvalidErrorString = _WmanIfBsPkmTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 3, 3, 1, 18),
    _WmanIfBsPkmTEKInvalidErrorString_Type()
)
wmanIfBsPkmTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPkmTEKInvalidErrorString.setStatus("current")
_WmanIfBsNotification_ObjectIdentity = ObjectIdentity
wmanIfBsNotification = _WmanIfBsNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4)
)
_WmanIfBsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanIfBsTrapDefinitions = _WmanIfBsTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1)
)
_WmanIfBsThresholdConfigTable_Object = MibTable
wmanIfBsThresholdConfigTable = _WmanIfBsThresholdConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfBsThresholdConfigTable.setStatus("current")
_WmanIfBsThresholdConfigEntry_Object = MibTableRow
wmanIfBsThresholdConfigEntry = _WmanIfBsThresholdConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1)
)
wmanIfBsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsThresholdConfigEntry.setStatus("current")
_WmanIfBsRssiLowThreshold_Type = Integer32
_WmanIfBsRssiLowThreshold_Object = MibTableColumn
wmanIfBsRssiLowThreshold = _WmanIfBsRssiLowThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 1),
    _WmanIfBsRssiLowThreshold_Type()
)
wmanIfBsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsRssiLowThreshold.setUnits("dBm")
_WmanIfBsRssiHighThreshold_Type = Integer32
_WmanIfBsRssiHighThreshold_Object = MibTableColumn
wmanIfBsRssiHighThreshold = _WmanIfBsRssiHighThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 2),
    _WmanIfBsRssiHighThreshold_Type()
)
wmanIfBsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsRssiHighThreshold.setUnits("dBm")
_WmanIfBsTempLowAlarmThreshold_Type = Integer32
_WmanIfBsTempLowAlarmThreshold_Object = MibTableColumn
wmanIfBsTempLowAlarmThreshold = _WmanIfBsTempLowAlarmThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 3),
    _WmanIfBsTempLowAlarmThreshold_Type()
)
wmanIfBsTempLowAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTempLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsTempLowAlarmThreshold.setUnits("degreeF")
_WmanIfBsTempLowAlarmRestoredThreshold_Type = Integer32
_WmanIfBsTempLowAlarmRestoredThreshold_Object = MibTableColumn
wmanIfBsTempLowAlarmRestoredThreshold = _WmanIfBsTempLowAlarmRestoredThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 4),
    _WmanIfBsTempLowAlarmRestoredThreshold_Type()
)
wmanIfBsTempLowAlarmRestoredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTempLowAlarmRestoredThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsTempLowAlarmRestoredThreshold.setUnits("degreeF")
_WmanIfBsTempHighAlarmThreshold_Type = Integer32
_WmanIfBsTempHighAlarmThreshold_Object = MibTableColumn
wmanIfBsTempHighAlarmThreshold = _WmanIfBsTempHighAlarmThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 5),
    _WmanIfBsTempHighAlarmThreshold_Type()
)
wmanIfBsTempHighAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTempHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsTempHighAlarmThreshold.setUnits("degreeF")
_WmanIfBsTempHighAlarmRestoredThreshold_Type = Integer32
_WmanIfBsTempHighAlarmRestoredThreshold_Object = MibTableColumn
wmanIfBsTempHighAlarmRestoredThreshold = _WmanIfBsTempHighAlarmRestoredThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 1, 1, 6),
    _WmanIfBsTempHighAlarmRestoredThreshold_Type()
)
wmanIfBsTempHighAlarmRestoredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTempHighAlarmRestoredThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfBsTempHighAlarmRestoredThreshold.setUnits("degreeF")
_WmanIfBsSsNotificationObjectsTable_Object = MibTable
wmanIfBsSsNotificationObjectsTable = _WmanIfBsSsNotificationObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfBsSsNotificationObjectsTable.setStatus("current")
_WmanIfBsSsNotificationObjectsEntry_Object = MibTableRow
wmanIfBsSsNotificationObjectsEntry = _WmanIfBsSsNotificationObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1)
)
wmanIfBsSsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTrapSsId"),
)
if mibBuilder.loadTexts:
    wmanIfBsSsNotificationObjectsEntry.setStatus("current")


class _WmanIfBsTrapSsId_Type(Unsigned32):
    """Custom type wmanIfBsTrapSsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfBsTrapSsId_Type.__name__ = "Unsigned32"
_WmanIfBsTrapSsId_Object = MibTableColumn
wmanIfBsTrapSsId = _WmanIfBsTrapSsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 1),
    _WmanIfBsTrapSsId_Type()
)
wmanIfBsTrapSsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsTrapSsId.setStatus("current")
_WmanIfBsSsNotMacAddr_Type = MacAddress
_WmanIfBsSsNotMacAddr_Object = MibTableColumn
wmanIfBsSsNotMacAddr = _WmanIfBsSsNotMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 2),
    _WmanIfBsSsNotMacAddr_Type()
)
wmanIfBsSsNotMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsNotMacAddr.setStatus("current")


class _WmanIfBsSsStatusValue_Type(Integer32):
    """Custom type wmanIfBsSsStatusValue based on Integer32"""
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
        *(("ssInitRangingSucc", 1),
          ("ssInitRangingFail", 2),
          ("ssRegistered", 3),
          ("ssRegistrationFail", 4),
          ("ssDeregistered", 5),
          ("ssBasicCapabilitySucc", 6),
          ("ssBasicCapabilityFail", 7),
          ("ssAuthorizationSucc", 8),
          ("ssAuthorizationFail", 9),
          ("tftpSucc", 10),
          ("tftpFail", 11),
          ("sfCreationSucc", 12),
          ("sfCreationFail", 13))
    )


_WmanIfBsSsStatusValue_Type.__name__ = "Integer32"
_WmanIfBsSsStatusValue_Object = MibTableColumn
wmanIfBsSsStatusValue = _WmanIfBsSsStatusValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 3),
    _WmanIfBsSsStatusValue_Type()
)
wmanIfBsSsStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsStatusValue.setStatus("current")
_WmanIfBsSsStatusInfo_Type = OctetString
_WmanIfBsSsStatusInfo_Object = MibTableColumn
wmanIfBsSsStatusInfo = _WmanIfBsSsStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 4),
    _WmanIfBsSsStatusInfo_Type()
)
wmanIfBsSsStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsStatusInfo.setStatus("current")


class _WmanIfBsDynamicServiceType_Type(Integer32):
    """Custom type wmanIfBsDynamicServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bsSfCreationReq", 1),
          ("bsSfCreationRsp", 2),
          ("bsSfCreationAck", 3))
    )


_WmanIfBsDynamicServiceType_Type.__name__ = "Integer32"
_WmanIfBsDynamicServiceType_Object = MibTableColumn
wmanIfBsDynamicServiceType = _WmanIfBsDynamicServiceType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 5),
    _WmanIfBsDynamicServiceType_Type()
)
wmanIfBsDynamicServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDynamicServiceType.setStatus("current")
_WmanIfBsDynamicServiceFailReason_Type = OctetString
_WmanIfBsDynamicServiceFailReason_Object = MibTableColumn
wmanIfBsDynamicServiceFailReason = _WmanIfBsDynamicServiceFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 6),
    _WmanIfBsDynamicServiceFailReason_Type()
)
wmanIfBsDynamicServiceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsDynamicServiceFailReason.setStatus("current")


class _WmanIfBsSsRssiStatus_Type(Integer32):
    """Custom type wmanIfBsSsRssiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bsRssiAlarm", 1),
          ("bsRssiNoAlarm", 2))
    )


_WmanIfBsSsRssiStatus_Type.__name__ = "Integer32"
_WmanIfBsSsRssiStatus_Object = MibTableColumn
wmanIfBsSsRssiStatus = _WmanIfBsSsRssiStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 7),
    _WmanIfBsSsRssiStatus_Type()
)
wmanIfBsSsRssiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRssiStatus.setStatus("current")
_WmanIfBsSsRssiStatusInfo_Type = OctetString
_WmanIfBsSsRssiStatusInfo_Object = MibTableColumn
wmanIfBsSsRssiStatusInfo = _WmanIfBsSsRssiStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 2, 1, 8),
    _WmanIfBsSsRssiStatusInfo_Type()
)
wmanIfBsSsRssiStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsSsRssiStatusInfo.setStatus("current")
_WmanIfBsNotificationObjectsTable_Object = MibTable
wmanIfBsNotificationObjectsTable = _WmanIfBsNotificationObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7)
)
if mibBuilder.loadTexts:
    wmanIfBsNotificationObjectsTable.setStatus("current")
_WmanIfBsNotificationObjectsEntry_Object = MibTableRow
wmanIfBsNotificationObjectsEntry = _WmanIfBsNotificationObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1)
)
wmanIfBsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfBsNotificationObjectsEntry.setStatus("current")


class _WmanIfBsPowerStatus_Type(Integer32):
    """Custom type wmanIfBsPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("priOnSecStandby", 0),
          ("secOnPriStandby", 1),
          ("priOnSecFailed", 2),
          ("secOnPriFailed", 3))
    )


_WmanIfBsPowerStatus_Type.__name__ = "Integer32"
_WmanIfBsPowerStatus_Object = MibTableColumn
wmanIfBsPowerStatus = _WmanIfBsPowerStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 1),
    _WmanIfBsPowerStatus_Type()
)
wmanIfBsPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPowerStatus.setStatus("current")


class _WmanIfBsFanStatus_Type(Integer32):
    """Custom type wmanIfBsFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanFail", 1),
          ("fanSucc", 2))
    )


_WmanIfBsFanStatus_Type.__name__ = "Integer32"
_WmanIfBsFanStatus_Object = MibTableColumn
wmanIfBsFanStatus = _WmanIfBsFanStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 2),
    _WmanIfBsFanStatus_Type()
)
wmanIfBsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsFanStatus.setStatus("current")


class _WmanIfBsTemperatureStatus_Type(Integer32):
    """Custom type wmanIfBsTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowTempReached", 1),
          ("highTempReached", 2),
          ("temperatureNormal", 3))
    )


_WmanIfBsTemperatureStatus_Type.__name__ = "Integer32"
_WmanIfBsTemperatureStatus_Object = MibTableColumn
wmanIfBsTemperatureStatus = _WmanIfBsTemperatureStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 3),
    _WmanIfBsTemperatureStatus_Type()
)
wmanIfBsTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsTemperatureStatus.setStatus("current")
_WmanIfBsPowerStatusInfo_Type = OctetString
_WmanIfBsPowerStatusInfo_Object = MibTableColumn
wmanIfBsPowerStatusInfo = _WmanIfBsPowerStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 4),
    _WmanIfBsPowerStatusInfo_Type()
)
wmanIfBsPowerStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsPowerStatusInfo.setStatus("current")
_WmanIfBsFanStatusInfo_Type = OctetString
_WmanIfBsFanStatusInfo_Object = MibTableColumn
wmanIfBsFanStatusInfo = _WmanIfBsFanStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 5),
    _WmanIfBsFanStatusInfo_Type()
)
wmanIfBsFanStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsFanStatusInfo.setStatus("current")
_WmanIfBsTemperatureStatusInfo_Type = OctetString
_WmanIfBsTemperatureStatusInfo_Object = MibTableColumn
wmanIfBsTemperatureStatusInfo = _WmanIfBsTemperatureStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 7, 1, 6),
    _WmanIfBsTemperatureStatusInfo_Type()
)
wmanIfBsTemperatureStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfBsTemperatureStatusInfo.setStatus("current")
_WmanIfBsTrapControl_ObjectIdentity = ObjectIdentity
wmanIfBsTrapControl = _WmanIfBsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2)
)


class _WmanIfBsTrapControlRegister_Type(Bits):
    """Custom type wmanIfBsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanBsSsStatusNotification", 0),
          ("wmanBsSsDynamicServiceFail", 1),
          ("wmanBsPowerStatusChange", 2),
          ("wmanBsFanStatusChange", 3),
          ("wmanBsTemperatureChange", 4),
          ("wmanBsSsRssiStatusChange", 5),
          ("wmanBsSsBPKMFail", 6))
    )

_WmanIfBsTrapControlRegister_Type.__name__ = "Bits"
_WmanIfBsTrapControlRegister_Object = MibScalar
wmanIfBsTrapControlRegister = _WmanIfBsTrapControlRegister_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 2, 1),
    _WmanIfBsTrapControlRegister_Type()
)
wmanIfBsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfBsTrapControlRegister.setStatus("current")
_WmanIfSsObjects_ObjectIdentity = ObjectIdentity
wmanIfSsObjects = _WmanIfSsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2)
)
_WmanIfSsCps_ObjectIdentity = ObjectIdentity
wmanIfSsCps = _WmanIfSsCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1)
)
_WmanIfSsConfigFileEncodingTable_Object = MibTable
wmanIfSsConfigFileEncodingTable = _WmanIfSsConfigFileEncodingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsConfigFileEncodingTable.setStatus("current")
_WmanIfSsConfigFileEncodingEntry_Object = MibTableRow
wmanIfSsConfigFileEncodingEntry = _WmanIfSsConfigFileEncodingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1)
)
wmanIfSsConfigFileEncodingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsConfigFileEncodingEntry.setStatus("current")


class _WmanIfSsMicConfigSetting_Type(OctetString):
    """Custom type wmanIfSsMicConfigSetting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_WmanIfSsMicConfigSetting_Type.__name__ = "OctetString"
_WmanIfSsMicConfigSetting_Object = MibTableColumn
wmanIfSsMicConfigSetting = _WmanIfSsMicConfigSetting_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 1),
    _WmanIfSsMicConfigSetting_Type()
)
wmanIfSsMicConfigSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsMicConfigSetting.setStatus("current")


class _WmanIfSsVendorId_Type(OctetString):
    """Custom type wmanIfSsVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_WmanIfSsVendorId_Type.__name__ = "OctetString"
_WmanIfSsVendorId_Object = MibTableColumn
wmanIfSsVendorId = _WmanIfSsVendorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 2),
    _WmanIfSsVendorId_Type()
)
wmanIfSsVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsVendorId.setStatus("current")
_WmanIfSsHwId_Type = OctetString
_WmanIfSsHwId_Object = MibTableColumn
wmanIfSsHwId = _WmanIfSsHwId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 3),
    _WmanIfSsHwId_Type()
)
wmanIfSsHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsHwId.setStatus("current")
_WmanIfSsSwVersion_Type = OctetString
_WmanIfSsSwVersion_Object = MibTableColumn
wmanIfSsSwVersion = _WmanIfSsSwVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 4),
    _WmanIfSsSwVersion_Type()
)
wmanIfSsSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsSwVersion.setStatus("current")
_WmanIfSsUpgradeFileName_Type = OctetString
_WmanIfSsUpgradeFileName_Object = MibTableColumn
wmanIfSsUpgradeFileName = _WmanIfSsUpgradeFileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 5),
    _WmanIfSsUpgradeFileName_Type()
)
wmanIfSsUpgradeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsUpgradeFileName.setStatus("current")
_WmanIfSsSwUpgradeTftpServer_Type = InetAddress
_WmanIfSsSwUpgradeTftpServer_Object = MibTableColumn
wmanIfSsSwUpgradeTftpServer = _WmanIfSsSwUpgradeTftpServer_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 6),
    _WmanIfSsSwUpgradeTftpServer_Type()
)
wmanIfSsSwUpgradeTftpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsSwUpgradeTftpServer.setStatus("current")
_WmanIfSsTftpServerTimeStamp_Type = DateAndTime
_WmanIfSsTftpServerTimeStamp_Object = MibTableColumn
wmanIfSsTftpServerTimeStamp = _WmanIfSsTftpServerTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 1, 1, 7),
    _WmanIfSsTftpServerTimeStamp_Type()
)
wmanIfSsTftpServerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsTftpServerTimeStamp.setStatus("current")
_WmanIfSsConfigurationTable_Object = MibTable
wmanIfSsConfigurationTable = _WmanIfSsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsConfigurationTable.setStatus("current")
_WmanIfSsConfigurationEntry_Object = MibTableRow
wmanIfSsConfigurationEntry = _WmanIfSsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1)
)
wmanIfSsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsConfigurationEntry.setStatus("current")


class _WmanIfSsLostDLMapInterval_Type(Integer32):
    """Custom type wmanIfSsLostDLMapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WmanIfSsLostDLMapInterval_Type.__name__ = "Integer32"
_WmanIfSsLostDLMapInterval_Object = MibTableColumn
wmanIfSsLostDLMapInterval = _WmanIfSsLostDLMapInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 1),
    _WmanIfSsLostDLMapInterval_Type()
)
wmanIfSsLostDLMapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsLostDLMapInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsLostDLMapInterval.setUnits("milliseconds")


class _WmanIfSsLostULMapInterval_Type(Integer32):
    """Custom type wmanIfSsLostULMapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WmanIfSsLostULMapInterval_Type.__name__ = "Integer32"
_WmanIfSsLostULMapInterval_Object = MibTableColumn
wmanIfSsLostULMapInterval = _WmanIfSsLostULMapInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 2),
    _WmanIfSsLostULMapInterval_Type()
)
wmanIfSsLostULMapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsLostULMapInterval.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsLostULMapInterval.setUnits("milliseconds")


class _WmanIfSsContentionRangRetries_Type(Integer32):
    """Custom type wmanIfSsContentionRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsContentionRangRetries_Type.__name__ = "Integer32"
_WmanIfSsContentionRangRetries_Object = MibTableColumn
wmanIfSsContentionRangRetries = _WmanIfSsContentionRangRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 3),
    _WmanIfSsContentionRangRetries_Type()
)
wmanIfSsContentionRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsContentionRangRetries.setStatus("current")


class _WmanIfSsRequestRetries_Type(Integer32):
    """Custom type wmanIfSsRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsRequestRetries_Object = MibTableColumn
wmanIfSsRequestRetries = _WmanIfSsRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 4),
    _WmanIfSsRequestRetries_Type()
)
wmanIfSsRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRequestRetries.setStatus("current")


class _WmanIfSsRegRequestRetries_Type(Integer32):
    """Custom type wmanIfSsRegRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsRegRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsRegRequestRetries_Object = MibTableColumn
wmanIfSsRegRequestRetries = _WmanIfSsRegRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 5),
    _WmanIfSsRegRequestRetries_Type()
)
wmanIfSsRegRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRegRequestRetries.setStatus("current")


class _WmanIfSsTftpBackoffStart_Type(Integer32):
    """Custom type wmanIfSsTftpBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfSsTftpBackoffStart_Type.__name__ = "Integer32"
_WmanIfSsTftpBackoffStart_Object = MibTableColumn
wmanIfSsTftpBackoffStart = _WmanIfSsTftpBackoffStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 6),
    _WmanIfSsTftpBackoffStart_Type()
)
wmanIfSsTftpBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffStart.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffStart.setUnits("seconds")


class _WmanIfSsTftpBackoffEnd_Type(Integer32):
    """Custom type wmanIfSsTftpBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsTftpBackoffEnd_Type.__name__ = "Integer32"
_WmanIfSsTftpBackoffEnd_Object = MibTableColumn
wmanIfSsTftpBackoffEnd = _WmanIfSsTftpBackoffEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 7),
    _WmanIfSsTftpBackoffEnd_Type()
)
wmanIfSsTftpBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffEnd.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpBackoffEnd.setUnits("seconds")


class _WmanIfSsTftpRequestRetries_Type(Integer32):
    """Custom type wmanIfSsTftpRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfSsTftpRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpRequestRetries_Object = MibTableColumn
wmanIfSsTftpRequestRetries = _WmanIfSsTftpRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 8),
    _WmanIfSsTftpRequestRetries_Type()
)
wmanIfSsTftpRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpRequestRetries.setStatus("current")


class _WmanIfSsTftpDownloadRetries_Type(Integer32):
    """Custom type wmanIfSsTftpDownloadRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsTftpDownloadRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpDownloadRetries_Object = MibTableColumn
wmanIfSsTftpDownloadRetries = _WmanIfSsTftpDownloadRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 9),
    _WmanIfSsTftpDownloadRetries_Type()
)
wmanIfSsTftpDownloadRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpDownloadRetries.setStatus("current")


class _WmanIfSsTftpWait_Type(Integer32):
    """Custom type wmanIfSsTftpWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WmanIfSsTftpWait_Type.__name__ = "Integer32"
_WmanIfSsTftpWait_Object = MibTableColumn
wmanIfSsTftpWait = _WmanIfSsTftpWait_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 10),
    _WmanIfSsTftpWait_Type()
)
wmanIfSsTftpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpWait.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsTftpWait.setUnits("minutes")


class _WmanIfSsToDRetries_Type(Integer32):
    """Custom type wmanIfSsToDRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_WmanIfSsToDRetries_Type.__name__ = "Integer32"
_WmanIfSsToDRetries_Object = MibTableColumn
wmanIfSsToDRetries = _WmanIfSsToDRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 11),
    _WmanIfSsToDRetries_Type()
)
wmanIfSsToDRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsToDRetries.setStatus("current")


class _WmanIfSsToDRetryPeriod_Type(Integer32):
    """Custom type wmanIfSsToDRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_WmanIfSsToDRetryPeriod_Type.__name__ = "Integer32"
_WmanIfSsToDRetryPeriod_Object = MibTableColumn
wmanIfSsToDRetryPeriod = _WmanIfSsToDRetryPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 12),
    _WmanIfSsToDRetryPeriod_Type()
)
wmanIfSsToDRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsToDRetryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsToDRetryPeriod.setUnits("minutes")


class _WmanIfSsT1Timeout_Type(Integer32):
    """Custom type wmanIfSsT1Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_WmanIfSsT1Timeout_Type.__name__ = "Integer32"
_WmanIfSsT1Timeout_Object = MibTableColumn
wmanIfSsT1Timeout = _WmanIfSsT1Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 13),
    _WmanIfSsT1Timeout_Type()
)
wmanIfSsT1Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT1Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT1Timeout.setUnits("milliseconds")


class _WmanIfSsT2Timeout_Type(Integer32):
    """Custom type wmanIfSsT2Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfSsT2Timeout_Type.__name__ = "Integer32"
_WmanIfSsT2Timeout_Object = MibTableColumn
wmanIfSsT2Timeout = _WmanIfSsT2Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 14),
    _WmanIfSsT2Timeout_Type()
)
wmanIfSsT2Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT2Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT2Timeout.setUnits("milliseconds")


class _WmanIfSsT3Timeout_Type(Integer32):
    """Custom type wmanIfSsT3Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsT3Timeout_Type.__name__ = "Integer32"
_WmanIfSsT3Timeout_Object = MibTableColumn
wmanIfSsT3Timeout = _WmanIfSsT3Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 15),
    _WmanIfSsT3Timeout_Type()
)
wmanIfSsT3Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT3Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT3Timeout.setUnits("milliseconds")


class _WmanIfSsT4Timeout_Type(Integer32):
    """Custom type wmanIfSsT4Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 35),
    )


_WmanIfSsT4Timeout_Type.__name__ = "Integer32"
_WmanIfSsT4Timeout_Object = MibTableColumn
wmanIfSsT4Timeout = _WmanIfSsT4Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 16),
    _WmanIfSsT4Timeout_Type()
)
wmanIfSsT4Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT4Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT4Timeout.setUnits("seconds")


class _WmanIfSsT6Timeout_Type(Integer32):
    """Custom type wmanIfSsT6Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIfSsT6Timeout_Type.__name__ = "Integer32"
_WmanIfSsT6Timeout_Object = MibTableColumn
wmanIfSsT6Timeout = _WmanIfSsT6Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 17),
    _WmanIfSsT6Timeout_Type()
)
wmanIfSsT6Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT6Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT6Timeout.setUnits("milliseconds")


class _WmanIfSsT12Timeout_Type(Integer32):
    """Custom type wmanIfSsT12Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_WmanIfSsT12Timeout_Type.__name__ = "Integer32"
_WmanIfSsT12Timeout_Object = MibTableColumn
wmanIfSsT12Timeout = _WmanIfSsT12Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 18),
    _WmanIfSsT12Timeout_Type()
)
wmanIfSsT12Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT12Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT12Timeout.setUnits("milliseconds")


class _WmanIfSsT14Timeout_Type(Integer32):
    """Custom type wmanIfSsT14Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsT14Timeout_Type.__name__ = "Integer32"
_WmanIfSsT14Timeout_Object = MibTableColumn
wmanIfSsT14Timeout = _WmanIfSsT14Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 19),
    _WmanIfSsT14Timeout_Type()
)
wmanIfSsT14Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT14Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT14Timeout.setUnits("milliseconds")


class _WmanIfSsT16Timeout_Type(Integer32):
    """Custom type wmanIfSsT16Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_WmanIfSsT16Timeout_Type.__name__ = "Integer32"
_WmanIfSsT16Timeout_Object = MibTableColumn
wmanIfSsT16Timeout = _WmanIfSsT16Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 20),
    _WmanIfSsT16Timeout_Type()
)
wmanIfSsT16Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT16Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT16Timeout.setUnits("milliseconds")


class _WmanIfSsT18Timeout_Type(Integer32):
    """Custom type wmanIfSsT18Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsT18Timeout_Type.__name__ = "Integer32"
_WmanIfSsT18Timeout_Object = MibTableColumn
wmanIfSsT18Timeout = _WmanIfSsT18Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 21),
    _WmanIfSsT18Timeout_Type()
)
wmanIfSsT18Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT18Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT18Timeout.setUnits("milliseconds")


class _WmanIfSsT19Timeout_Type(Integer32):
    """Custom type wmanIfSsT19Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsT19Timeout_Type.__name__ = "Integer32"
_WmanIfSsT19Timeout_Object = MibTableColumn
wmanIfSsT19Timeout = _WmanIfSsT19Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 22),
    _WmanIfSsT19Timeout_Type()
)
wmanIfSsT19Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT19Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT19Timeout.setUnits("seconds")


class _WmanIfSsT20Timeout_Type(Integer32):
    """Custom type wmanIfSsT20Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfSsT20Timeout_Type.__name__ = "Integer32"
_WmanIfSsT20Timeout_Object = MibTableColumn
wmanIfSsT20Timeout = _WmanIfSsT20Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 23),
    _WmanIfSsT20Timeout_Type()
)
wmanIfSsT20Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT20Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT20Timeout.setUnits("milliseconds")


class _WmanIfSsT21Timeout_Type(Integer32):
    """Custom type wmanIfSsT21Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WmanIfSsT21Timeout_Type.__name__ = "Integer32"
_WmanIfSsT21Timeout_Object = MibTableColumn
wmanIfSsT21Timeout = _WmanIfSsT21Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 24),
    _WmanIfSsT21Timeout_Type()
)
wmanIfSsT21Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT21Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT21Timeout.setUnits("milliseconds")


class _WmanIfSsSBCRequestRetries_Type(Integer32):
    """Custom type wmanIfSsSBCRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIfSsSBCRequestRetries_Type.__name__ = "Integer32"
_WmanIfSsSBCRequestRetries_Object = MibTableColumn
wmanIfSsSBCRequestRetries = _WmanIfSsSBCRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 25),
    _WmanIfSsSBCRequestRetries_Type()
)
wmanIfSsSBCRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsSBCRequestRetries.setStatus("current")


class _WmanIfSsTftpCpltRetries_Type(Integer32):
    """Custom type wmanIfSsTftpCpltRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_WmanIfSsTftpCpltRetries_Type.__name__ = "Integer32"
_WmanIfSsTftpCpltRetries_Object = MibTableColumn
wmanIfSsTftpCpltRetries = _WmanIfSsTftpCpltRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 26),
    _WmanIfSsTftpCpltRetries_Type()
)
wmanIfSsTftpCpltRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTftpCpltRetries.setStatus("current")


class _WmanIfSsT26Timeout_Type(Integer32):
    """Custom type wmanIfSsT26Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_WmanIfSsT26Timeout_Type.__name__ = "Integer32"
_WmanIfSsT26Timeout_Object = MibTableColumn
wmanIfSsT26Timeout = _WmanIfSsT26Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 27),
    _WmanIfSsT26Timeout_Type()
)
wmanIfSsT26Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsT26Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsT26Timeout.setUnits("milliseconds")


class _WmanIfSsDLManagProcTime_Type(Integer32):
    """Custom type wmanIfSsDLManagProcTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WmanIfSsDLManagProcTime_Type.__name__ = "Integer32"
_WmanIfSsDLManagProcTime_Object = MibTableColumn
wmanIfSsDLManagProcTime = _WmanIfSsDLManagProcTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 1, 2, 1, 28),
    _WmanIfSsDLManagProcTime_Type()
)
wmanIfSsDLManagProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsDLManagProcTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsDLManagProcTime.setUnits("micro seconds")
_WmanIfSsPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfSsPkmObjects = _WmanIfSsPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2)
)
_WmanIfSsPkmBaseTable_Object = MibTable
wmanIfSsPkmBaseTable = _WmanIfSsPkmBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfSsPkmBaseTable.setStatus("current")
_WmanIfSsPkmBaseEntry_Object = MibTableRow
wmanIfSsPkmBaseEntry = _WmanIfSsPkmBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1)
)
wmanIfSsPkmBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsPkmBaseEntry.setStatus("current")
_WmanIfSsPkmPrivacyEnable_Type = TruthValue
_WmanIfSsPkmPrivacyEnable_Object = MibTableColumn
wmanIfSsPkmPrivacyEnable = _WmanIfSsPkmPrivacyEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 1),
    _WmanIfSsPkmPrivacyEnable_Type()
)
wmanIfSsPkmPrivacyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmPrivacyEnable.setStatus("current")


class _WmanIfSsPkmPublicKey_Type(OctetString):
    """Custom type wmanIfSsPkmPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(140, 140),
    )
    fixedLength = 140


_WmanIfSsPkmPublicKey_Type.__name__ = "OctetString"
_WmanIfSsPkmPublicKey_Object = MibTableColumn
wmanIfSsPkmPublicKey = _WmanIfSsPkmPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 2),
    _WmanIfSsPkmPublicKey_Type()
)
wmanIfSsPkmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmPublicKey.setStatus("current")


class _WmanIfSsPkmAuthGraceTime_Type(Integer32):
    """Custom type wmanIfSsPkmAuthGraceTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3024000),
    )


_WmanIfSsPkmAuthGraceTime_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthGraceTime_Object = MibTableColumn
wmanIfSsPkmAuthGraceTime = _WmanIfSsPkmAuthGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 3),
    _WmanIfSsPkmAuthGraceTime_Type()
)
wmanIfSsPkmAuthGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthGraceTime.setUnits("seconds")


class _WmanIfSsPkmTEKGraceTime_Type(Integer32):
    """Custom type wmanIfSsPkmTEKGraceTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 302399),
    )


_WmanIfSsPkmTEKGraceTime_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKGraceTime_Object = MibTableColumn
wmanIfSsPkmTEKGraceTime = _WmanIfSsPkmTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 4),
    _WmanIfSsPkmTEKGraceTime_Type()
)
wmanIfSsPkmTEKGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKGraceTime.setUnits("seconds")


class _WmanIfSsPkmAuthWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmAuthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIfSsPkmAuthWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthWaitTimeout_Object = MibTableColumn
wmanIfSsPkmAuthWaitTimeout = _WmanIfSsPkmAuthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 5),
    _WmanIfSsPkmAuthWaitTimeout_Type()
)
wmanIfSsPkmAuthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmReauthWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmReauthWaitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WmanIfSsPkmReauthWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmReauthWaitTimeout_Object = MibTableColumn
wmanIfSsPkmReauthWaitTimeout = _WmanIfSsPkmReauthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 6),
    _WmanIfSsPkmReauthWaitTimeout_Type()
)
wmanIfSsPkmReauthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmReauthWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmOpWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmOpWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfSsPkmOpWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmOpWaitTimeout_Object = MibTableColumn
wmanIfSsPkmOpWaitTimeout = _WmanIfSsPkmOpWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 7),
    _WmanIfSsPkmOpWaitTimeout_Type()
)
wmanIfSsPkmOpWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmOpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmOpWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmRekeyWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmRekeyWaitTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WmanIfSsPkmRekeyWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmRekeyWaitTimeout_Object = MibTableColumn
wmanIfSsPkmRekeyWaitTimeout = _WmanIfSsPkmRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 8),
    _WmanIfSsPkmRekeyWaitTimeout_Type()
)
wmanIfSsPkmRekeyWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmRekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmRekeyWaitTimeout.setUnits("seconds")


class _WmanIfSsPkmAuthRejectWaitTimeout_Type(Integer32):
    """Custom type wmanIfSsPkmAuthRejectWaitTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WmanIfSsPkmAuthRejectWaitTimeout_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthRejectWaitTimeout_Object = MibTableColumn
wmanIfSsPkmAuthRejectWaitTimeout = _WmanIfSsPkmAuthRejectWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 1, 1, 9),
    _WmanIfSsPkmAuthRejectWaitTimeout_Type()
)
wmanIfSsPkmAuthRejectWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectWaitTimeout.setUnits("seconds")
_WmanIfSsPkmAuthTable_Object = MibTable
wmanIfSsPkmAuthTable = _WmanIfSsPkmAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthTable.setStatus("current")
_WmanIfSsPkmAuthEntry_Object = MibTableRow
wmanIfSsPkmAuthEntry = _WmanIfSsPkmAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1)
)
wmanIfSsPkmAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthEntry.setStatus("current")


class _WmanIfSsPkmAuthState_Type(Integer32):
    """Custom type wmanIfSsPkmAuthState based on Integer32"""
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
        *(("start", 1),
          ("authWait", 2),
          ("authorized", 3),
          ("reauthWait", 4),
          ("authRejectWait", 5),
          ("silent", 6))
    )


_WmanIfSsPkmAuthState_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthState_Object = MibTableColumn
wmanIfSsPkmAuthState = _WmanIfSsPkmAuthState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 1),
    _WmanIfSsPkmAuthState_Type()
)
wmanIfSsPkmAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthState.setStatus("current")


class _WmanIfSsPkmAuthKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfSsPkmAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WmanIfSsPkmAuthKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthKeySequenceNumber_Object = MibTableColumn
wmanIfSsPkmAuthKeySequenceNumber = _WmanIfSsPkmAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 2),
    _WmanIfSsPkmAuthKeySequenceNumber_Type()
)
wmanIfSsPkmAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthKeySequenceNumber.setStatus("current")
_WmanIfSsPkmAuthExpiresOld_Type = DateAndTime
_WmanIfSsPkmAuthExpiresOld_Object = MibTableColumn
wmanIfSsPkmAuthExpiresOld = _WmanIfSsPkmAuthExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 3),
    _WmanIfSsPkmAuthExpiresOld_Type()
)
wmanIfSsPkmAuthExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthExpiresOld.setStatus("current")
_WmanIfSsPkmAuthExpiresNew_Type = DateAndTime
_WmanIfSsPkmAuthExpiresNew_Object = MibTableColumn
wmanIfSsPkmAuthExpiresNew = _WmanIfSsPkmAuthExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 4),
    _WmanIfSsPkmAuthExpiresNew_Type()
)
wmanIfSsPkmAuthExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthExpiresNew.setStatus("current")
_WmanIfSsPkmAuthReset_Type = TruthValue
_WmanIfSsPkmAuthReset_Object = MibTableColumn
wmanIfSsPkmAuthReset = _WmanIfSsPkmAuthReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 5),
    _WmanIfSsPkmAuthReset_Type()
)
wmanIfSsPkmAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthReset.setStatus("current")
_WmanIfSsPkmAuthentInfos_Type = Counter32
_WmanIfSsPkmAuthentInfos_Object = MibTableColumn
wmanIfSsPkmAuthentInfos = _WmanIfSsPkmAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 6),
    _WmanIfSsPkmAuthentInfos_Type()
)
wmanIfSsPkmAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthentInfos.setStatus("current")
_WmanIfSsPkmAuthRequests_Type = Counter32
_WmanIfSsPkmAuthRequests_Object = MibTableColumn
wmanIfSsPkmAuthRequests = _WmanIfSsPkmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 7),
    _WmanIfSsPkmAuthRequests_Type()
)
wmanIfSsPkmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRequests.setStatus("current")
_WmanIfSsPkmAuthReplies_Type = Counter32
_WmanIfSsPkmAuthReplies_Object = MibTableColumn
wmanIfSsPkmAuthReplies = _WmanIfSsPkmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 8),
    _WmanIfSsPkmAuthReplies_Type()
)
wmanIfSsPkmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthReplies.setStatus("current")
_WmanIfSsPkmAuthRejects_Type = Counter32
_WmanIfSsPkmAuthRejects_Object = MibTableColumn
wmanIfSsPkmAuthRejects = _WmanIfSsPkmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 9),
    _WmanIfSsPkmAuthRejects_Type()
)
wmanIfSsPkmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejects.setStatus("current")
_WmanIfSsPkmAuthInvalids_Type = Counter32
_WmanIfSsPkmAuthInvalids_Object = MibTableColumn
wmanIfSsPkmAuthInvalids = _WmanIfSsPkmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 10),
    _WmanIfSsPkmAuthInvalids_Type()
)
wmanIfSsPkmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalids.setStatus("current")


class _WmanIfSsPkmAuthRejectErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSs", 3),
          ("unauthorizedSaid", 4),
          ("permanentAuthorizationFailure", 8),
          ("timeOfDayNotAcquired", 11))
    )


_WmanIfSsPkmAuthRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthRejectErrorCode_Object = MibTableColumn
wmanIfSsPkmAuthRejectErrorCode = _WmanIfSsPkmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 11),
    _WmanIfSsPkmAuthRejectErrorCode_Type()
)
wmanIfSsPkmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectErrorCode.setStatus("current")


class _WmanIfSsPkmAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmAuthRejectErrorString_Object = MibTableColumn
wmanIfSsPkmAuthRejectErrorString = _WmanIfSsPkmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 12),
    _WmanIfSsPkmAuthRejectErrorString_Type()
)
wmanIfSsPkmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthRejectErrorString.setStatus("current")


class _WmanIfSsPkmAuthInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSs", 3),
          ("unsolicited", 5),
          ("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7))
    )


_WmanIfSsPkmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmAuthInvalidErrorCode_Object = MibTableColumn
wmanIfSsPkmAuthInvalidErrorCode = _WmanIfSsPkmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 13),
    _WmanIfSsPkmAuthInvalidErrorCode_Type()
)
wmanIfSsPkmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalidErrorCode.setStatus("current")


class _WmanIfSsPkmAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmAuthInvalidErrorString_Object = MibTableColumn
wmanIfSsPkmAuthInvalidErrorString = _WmanIfSsPkmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 2, 1, 14),
    _WmanIfSsPkmAuthInvalidErrorString_Type()
)
wmanIfSsPkmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmAuthInvalidErrorString.setStatus("current")
_WmanIfSsPkmTEKTable_Object = MibTable
wmanIfSsPkmTEKTable = _WmanIfSsPkmTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKTable.setStatus("current")
_WmanIfSsPkmTEKEntry_Object = MibTableRow
wmanIfSsPkmTEKEntry = _WmanIfSsPkmTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1)
)
wmanIfSsPkmTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfSsPkmTEKSAId"),
)
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKEntry.setStatus("current")


class _WmanIfSsPkmTEKSAId_Type(Integer32):
    """Custom type wmanIfSsPkmTEKSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_WmanIfSsPkmTEKSAId_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKSAId_Object = MibTableColumn
wmanIfSsPkmTEKSAId = _WmanIfSsPkmTEKSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 1),
    _WmanIfSsPkmTEKSAId_Type()
)
wmanIfSsPkmTEKSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKSAId.setStatus("current")


class _WmanIfSsPkmTEKSAType_Type(Integer32):
    """Custom type wmanIfSsPkmTEKSAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primarySA", 0),
          ("staticSA", 1),
          ("dynamicSA", 2))
    )


_WmanIfSsPkmTEKSAType_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKSAType_Object = MibTableColumn
wmanIfSsPkmTEKSAType = _WmanIfSsPkmTEKSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 2),
    _WmanIfSsPkmTEKSAType_Type()
)
wmanIfSsPkmTEKSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKSAType.setStatus("current")


class _WmanIfSsPkmTEKDataEncryptAlg_Type(Integer32):
    """Custom type wmanIfSsPkmTEKDataEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des56CbcMode", 1))
    )


_WmanIfSsPkmTEKDataEncryptAlg_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKDataEncryptAlg_Object = MibTableColumn
wmanIfSsPkmTEKDataEncryptAlg = _WmanIfSsPkmTEKDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 3),
    _WmanIfSsPkmTEKDataEncryptAlg_Type()
)
wmanIfSsPkmTEKDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKDataEncryptAlg.setStatus("current")


class _WmanIfSsPkmTEKDataAuthentAlg_Type(Integer32):
    """Custom type wmanIfSsPkmTEKDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_WmanIfSsPkmTEKDataAuthentAlg_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKDataAuthentAlg_Object = MibTableColumn
wmanIfSsPkmTEKDataAuthentAlg = _WmanIfSsPkmTEKDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 4),
    _WmanIfSsPkmTEKDataAuthentAlg_Type()
)
wmanIfSsPkmTEKDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKDataAuthentAlg.setStatus("current")


class _WmanIfSsPkmTEKEncryptAlg_Type(Integer32):
    """Custom type wmanIfSsPkmTEKEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tripleDES", 0),
          ("rsa1024", 1))
    )


_WmanIfSsPkmTEKEncryptAlg_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKEncryptAlg_Object = MibTableColumn
wmanIfSsPkmTEKEncryptAlg = _WmanIfSsPkmTEKEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 5),
    _WmanIfSsPkmTEKEncryptAlg_Type()
)
wmanIfSsPkmTEKEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKEncryptAlg.setStatus("current")


class _WmanIfSsPkmTEKState_Type(Integer32):
    """Custom type wmanIfSsPkmTEKState based on Integer32"""
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
        *(("start", 1),
          ("opWait", 2),
          ("opReauthWait", 3),
          ("operational", 4),
          ("rekeyWait", 5),
          ("rekeyReauthWait", 6))
    )


_WmanIfSsPkmTEKState_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKState_Object = MibTableColumn
wmanIfSsPkmTEKState = _WmanIfSsPkmTEKState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 6),
    _WmanIfSsPkmTEKState_Type()
)
wmanIfSsPkmTEKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKState.setStatus("current")


class _WmanIfSsPkmTEKKeySequenceNumber_Type(Integer32):
    """Custom type wmanIfSsPkmTEKKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WmanIfSsPkmTEKKeySequenceNumber_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKKeySequenceNumber_Object = MibTableColumn
wmanIfSsPkmTEKKeySequenceNumber = _WmanIfSsPkmTEKKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 7),
    _WmanIfSsPkmTEKKeySequenceNumber_Type()
)
wmanIfSsPkmTEKKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeySequenceNumber.setStatus("current")
_WmanIfSsPkmTEKExpiresOld_Type = DateAndTime
_WmanIfSsPkmTEKExpiresOld_Object = MibTableColumn
wmanIfSsPkmTEKExpiresOld = _WmanIfSsPkmTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 8),
    _WmanIfSsPkmTEKExpiresOld_Type()
)
wmanIfSsPkmTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKExpiresOld.setStatus("current")
_WmanIfSsPkmTEKExpiresNew_Type = DateAndTime
_WmanIfSsPkmTEKExpiresNew_Object = MibTableColumn
wmanIfSsPkmTEKExpiresNew = _WmanIfSsPkmTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 9),
    _WmanIfSsPkmTEKExpiresNew_Type()
)
wmanIfSsPkmTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKExpiresNew.setStatus("current")
_WmanIfSsPkmTEKKeyRequests_Type = Counter32
_WmanIfSsPkmTEKKeyRequests_Object = MibTableColumn
wmanIfSsPkmTEKKeyRequests = _WmanIfSsPkmTEKKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 10),
    _WmanIfSsPkmTEKKeyRequests_Type()
)
wmanIfSsPkmTEKKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeyRequests.setStatus("current")
_WmanIfSsPkmTEKKeyReplies_Type = Counter32
_WmanIfSsPkmTEKKeyReplies_Object = MibTableColumn
wmanIfSsPkmTEKKeyReplies = _WmanIfSsPkmTEKKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 11),
    _WmanIfSsPkmTEKKeyReplies_Type()
)
wmanIfSsPkmTEKKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeyReplies.setStatus("current")
_WmanIfSsPkmTEKKeyRejects_Type = Counter32
_WmanIfSsPkmTEKKeyRejects_Object = MibTableColumn
wmanIfSsPkmTEKKeyRejects = _WmanIfSsPkmTEKKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 12),
    _WmanIfSsPkmTEKKeyRejects_Type()
)
wmanIfSsPkmTEKKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeyRejects.setStatus("current")
_WmanIfSsPkmTEKInvalids_Type = Counter32
_WmanIfSsPkmTEKInvalids_Object = MibTableColumn
wmanIfSsPkmTEKInvalids = _WmanIfSsPkmTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 13),
    _WmanIfSsPkmTEKInvalids_Type()
)
wmanIfSsPkmTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKInvalids.setStatus("current")
_WmanIfSsPkmTEKAuthPends_Type = Counter32
_WmanIfSsPkmTEKAuthPends_Object = MibTableColumn
wmanIfSsPkmTEKAuthPends = _WmanIfSsPkmTEKAuthPends_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 14),
    _WmanIfSsPkmTEKAuthPends_Type()
)
wmanIfSsPkmTEKAuthPends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKAuthPends.setStatus("current")


class _WmanIfSsPkmTEKKeyRejectErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmTEKKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSaid", 4))
    )


_WmanIfSsPkmTEKKeyRejectErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKKeyRejectErrorCode_Object = MibTableColumn
wmanIfSsPkmTEKKeyRejectErrorCode = _WmanIfSsPkmTEKKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 15),
    _WmanIfSsPkmTEKKeyRejectErrorCode_Type()
)
wmanIfSsPkmTEKKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeyRejectErrorCode.setStatus("current")


class _WmanIfSsPkmTEKKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmTEKKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmTEKKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmTEKKeyRejectErrorString_Object = MibTableColumn
wmanIfSsPkmTEKKeyRejectErrorString = _WmanIfSsPkmTEKKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 16),
    _WmanIfSsPkmTEKKeyRejectErrorString_Type()
)
wmanIfSsPkmTEKKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKKeyRejectErrorString.setStatus("current")


class _WmanIfSsPkmTEKInvalidErrorCode_Type(Integer32):
    """Custom type wmanIfSsPkmTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("invalidKeySequence", 6))
    )


_WmanIfSsPkmTEKInvalidErrorCode_Type.__name__ = "Integer32"
_WmanIfSsPkmTEKInvalidErrorCode_Object = MibTableColumn
wmanIfSsPkmTEKInvalidErrorCode = _WmanIfSsPkmTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 17),
    _WmanIfSsPkmTEKInvalidErrorCode_Type()
)
wmanIfSsPkmTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKInvalidErrorCode.setStatus("current")


class _WmanIfSsPkmTEKInvalidErrorString_Type(SnmpAdminString):
    """Custom type wmanIfSsPkmTEKInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WmanIfSsPkmTEKInvalidErrorString_Type.__name__ = "SnmpAdminString"
_WmanIfSsPkmTEKInvalidErrorString_Object = MibTableColumn
wmanIfSsPkmTEKInvalidErrorString = _WmanIfSsPkmTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 3, 1, 18),
    _WmanIfSsPkmTEKInvalidErrorString_Type()
)
wmanIfSsPkmTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsPkmTEKInvalidErrorString.setStatus("current")
_WmanIfSsDeviceCertTable_Object = MibTable
wmanIfSsDeviceCertTable = _WmanIfSsDeviceCertTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    wmanIfSsDeviceCertTable.setStatus("current")
_WmanIfSsDeviceCertEntry_Object = MibTableRow
wmanIfSsDeviceCertEntry = _WmanIfSsDeviceCertEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 4, 1)
)
wmanIfSsDeviceCertEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsDeviceCertEntry.setStatus("current")
_WmanIfSsDeviceCert_Type = OctetString
_WmanIfSsDeviceCert_Object = MibTableColumn
wmanIfSsDeviceCert = _WmanIfSsDeviceCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 4, 1, 1),
    _WmanIfSsDeviceCert_Type()
)
wmanIfSsDeviceCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDeviceCert.setStatus("current")
_WmanIfSsDeviceManufCert_Type = OctetString
_WmanIfSsDeviceManufCert_Object = MibTableColumn
wmanIfSsDeviceManufCert = _WmanIfSsDeviceManufCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 2, 4, 1, 2),
    _WmanIfSsDeviceManufCert_Type()
)
wmanIfSsDeviceManufCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDeviceManufCert.setStatus("current")
_WmanIfSsNotification_ObjectIdentity = ObjectIdentity
wmanIfSsNotification = _WmanIfSsNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3)
)
_WmanIfSsTrapDefinitions_ObjectIdentity = ObjectIdentity
wmanIfSsTrapDefinitions = _WmanIfSsTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1)
)
_WmanIfSsNotificationObjectsTable_Object = MibTable
wmanIfSsNotificationObjectsTable = _WmanIfSsNotificationObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    wmanIfSsNotificationObjectsTable.setStatus("current")
_WmanIfSsNotificationObjectsEntry_Object = MibTableRow
wmanIfSsNotificationObjectsEntry = _WmanIfSsNotificationObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1)
)
wmanIfSsNotificationObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsNotificationObjectsEntry.setStatus("current")
_WmanIfSsMacAddress_Type = MacAddress
_WmanIfSsMacAddress_Object = MibTableColumn
wmanIfSsMacAddress = _WmanIfSsMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 1),
    _WmanIfSsMacAddress_Type()
)
wmanIfSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsMacAddress.setStatus("current")
_WmanIfSsUnknownTlv_Type = OctetString
_WmanIfSsUnknownTlv_Object = MibTableColumn
wmanIfSsUnknownTlv = _WmanIfSsUnknownTlv_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 2),
    _WmanIfSsUnknownTlv_Type()
)
wmanIfSsUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsUnknownTlv.setStatus("current")


class _WmanIfSsDynamicServiceType_Type(Integer32):
    """Custom type wmanIfSsDynamicServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssSfCreationReq", 1),
          ("ssSfCreationRsp", 2),
          ("ssSfCreationAck", 3))
    )


_WmanIfSsDynamicServiceType_Type.__name__ = "Integer32"
_WmanIfSsDynamicServiceType_Object = MibTableColumn
wmanIfSsDynamicServiceType = _WmanIfSsDynamicServiceType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 3),
    _WmanIfSsDynamicServiceType_Type()
)
wmanIfSsDynamicServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDynamicServiceType.setStatus("current")
_WmanIfSsDynamicServiceFailReason_Type = OctetString
_WmanIfSsDynamicServiceFailReason_Object = MibTableColumn
wmanIfSsDynamicServiceFailReason = _WmanIfSsDynamicServiceFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 4),
    _WmanIfSsDynamicServiceFailReason_Type()
)
wmanIfSsDynamicServiceFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsDynamicServiceFailReason.setStatus("current")


class _WmanIfSsRssiStatus_Type(Integer32):
    """Custom type wmanIfSsRssiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssRssiAlarm", 1),
          ("ssRssiNoAlarm", 2))
    )


_WmanIfSsRssiStatus_Type.__name__ = "Integer32"
_WmanIfSsRssiStatus_Object = MibTableColumn
wmanIfSsRssiStatus = _WmanIfSsRssiStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 5),
    _WmanIfSsRssiStatus_Type()
)
wmanIfSsRssiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsRssiStatus.setStatus("current")
_WmanIfSsRssiStatusInfo_Type = OctetString
_WmanIfSsRssiStatusInfo_Object = MibTableColumn
wmanIfSsRssiStatusInfo = _WmanIfSsRssiStatusInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 5, 1, 6),
    _WmanIfSsRssiStatusInfo_Type()
)
wmanIfSsRssiStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfSsRssiStatusInfo.setStatus("current")
_WmanIfSsTrapControl_ObjectIdentity = ObjectIdentity
wmanIfSsTrapControl = _WmanIfSsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2)
)


class _WmanIfSsTrapControlRegister_Type(Bits):
    """Custom type wmanIfSsTrapControlRegister based on Bits"""
    namedValues = NamedValues(
        *(("wmanSsTLVUnknown", 0),
          ("wmanSsDynamicServiceFail", 1),
          ("wmanSsDHCPSuccess", 2),
          ("wmanSsRssiStatusChange", 3))
    )

_WmanIfSsTrapControlRegister_Type.__name__ = "Bits"
_WmanIfSsTrapControlRegister_Object = MibScalar
wmanIfSsTrapControlRegister = _WmanIfSsTrapControlRegister_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 1),
    _WmanIfSsTrapControlRegister_Type()
)
wmanIfSsTrapControlRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsTrapControlRegister.setStatus("current")
_WmanIfSsThresholdConfigTable_Object = MibTable
wmanIfSsThresholdConfigTable = _WmanIfSsThresholdConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfSsThresholdConfigTable.setStatus("current")
_WmanIfSsThresholdConfigEntry_Object = MibTableRow
wmanIfSsThresholdConfigEntry = _WmanIfSsThresholdConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 2, 1)
)
wmanIfSsThresholdConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfSsThresholdConfigEntry.setStatus("current")
_WmanIfSsRssiLowThreshold_Type = Integer32
_WmanIfSsRssiLowThreshold_Object = MibTableColumn
wmanIfSsRssiLowThreshold = _WmanIfSsRssiLowThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 2, 1, 1),
    _WmanIfSsRssiLowThreshold_Type()
)
wmanIfSsRssiLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRssiLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsRssiLowThreshold.setUnits("dBm")
_WmanIfSsRssiHighThreshold_Type = Integer32
_WmanIfSsRssiHighThreshold_Object = MibTableColumn
wmanIfSsRssiHighThreshold = _WmanIfSsRssiHighThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 2, 2, 1, 2),
    _WmanIfSsRssiHighThreshold_Type()
)
wmanIfSsRssiHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfSsRssiHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfSsRssiHighThreshold.setUnits("dBm")
_WmanIfCommonObjects_ObjectIdentity = ObjectIdentity
wmanIfCommonObjects = _WmanIfCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3)
)
_WmanIfCmnPacketCs_ObjectIdentity = ObjectIdentity
wmanIfCmnPacketCs = _WmanIfCmnPacketCs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1)
)
_WmanIfCmnClassifierRuleTable_Object = MibTable
wmanIfCmnClassifierRuleTable = _WmanIfCmnClassifierRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleTable.setStatus("current")
_WmanIfCmnClassifierRuleEntry_Object = MibTableRow
wmanIfCmnClassifierRuleEntry = _WmanIfCmnClassifierRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1)
)
wmanIfCmnClassifierRuleEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnClassifierRuleIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnCpsSfIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEntry.setStatus("current")


class _WmanIfCmnClassifierRuleIndex_Type(Unsigned32):
    """Custom type wmanIfCmnClassifierRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnClassifierRuleIndex_Type.__name__ = "Unsigned32"
_WmanIfCmnClassifierRuleIndex_Object = MibTableColumn
wmanIfCmnClassifierRuleIndex = _WmanIfCmnClassifierRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 1),
    _WmanIfCmnClassifierRuleIndex_Type()
)
wmanIfCmnClassifierRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIndex.setStatus("current")


class _WmanIfCmnCpsSfIndex_Type(Unsigned32):
    """Custom type wmanIfCmnCpsSfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnCpsSfIndex_Type.__name__ = "Unsigned32"
_WmanIfCmnCpsSfIndex_Object = MibTableColumn
wmanIfCmnCpsSfIndex = _WmanIfCmnCpsSfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 2),
    _WmanIfCmnCpsSfIndex_Type()
)
wmanIfCmnCpsSfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfIndex.setStatus("current")


class _WmanIfCmnClassifierRulePriority_Type(Integer32):
    """Custom type wmanIfCmnClassifierRulePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRulePriority_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRulePriority_Object = MibTableColumn
wmanIfCmnClassifierRulePriority = _WmanIfCmnClassifierRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 3),
    _WmanIfCmnClassifierRulePriority_Type()
)
wmanIfCmnClassifierRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRulePriority.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosLow_Type(OctetString):
    """Custom type wmanIfCmnClassifierRuleIpTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfCmnClassifierRuleIpTosLow_Type.__name__ = "OctetString"
_WmanIfCmnClassifierRuleIpTosLow_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosLow = _WmanIfCmnClassifierRuleIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 4),
    _WmanIfCmnClassifierRuleIpTosLow_Type()
)
wmanIfCmnClassifierRuleIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosLow.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosHigh_Type(OctetString):
    """Custom type wmanIfCmnClassifierRuleIpTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfCmnClassifierRuleIpTosHigh_Type.__name__ = "OctetString"
_WmanIfCmnClassifierRuleIpTosHigh_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosHigh = _WmanIfCmnClassifierRuleIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 5),
    _WmanIfCmnClassifierRuleIpTosHigh_Type()
)
wmanIfCmnClassifierRuleIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosHigh.setStatus("current")


class _WmanIfCmnClassifierRuleIpTosMask_Type(OctetString):
    """Custom type wmanIfCmnClassifierRuleIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_WmanIfCmnClassifierRuleIpTosMask_Type.__name__ = "OctetString"
_WmanIfCmnClassifierRuleIpTosMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpTosMask = _WmanIfCmnClassifierRuleIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 6),
    _WmanIfCmnClassifierRuleIpTosMask_Type()
)
wmanIfCmnClassifierRuleIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpTosMask.setStatus("current")


class _WmanIfCmnClassifierRuleIpProtocol_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnClassifierRuleIpProtocol_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleIpProtocol_Object = MibTableColumn
wmanIfCmnClassifierRuleIpProtocol = _WmanIfCmnClassifierRuleIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 7),
    _WmanIfCmnClassifierRuleIpProtocol_Type()
)
wmanIfCmnClassifierRuleIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpProtocol.setStatus("current")
_WmanIfCmnClassifierRuleIpAddressType_Type = InetAddressType
_WmanIfCmnClassifierRuleIpAddressType_Object = MibTableColumn
wmanIfCmnClassifierRuleIpAddressType = _WmanIfCmnClassifierRuleIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 8),
    _WmanIfCmnClassifierRuleIpAddressType_Type()
)
wmanIfCmnClassifierRuleIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpAddressType.setStatus("current")
_WmanIfCmnClassifierRuleIpSourceAddr_Type = InetAddress
_WmanIfCmnClassifierRuleIpSourceAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleIpSourceAddr = _WmanIfCmnClassifierRuleIpSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 9),
    _WmanIfCmnClassifierRuleIpSourceAddr_Type()
)
wmanIfCmnClassifierRuleIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpSourceAddr.setStatus("current")
_WmanIfCmnClassifierRuleIpSourceMask_Type = InetAddress
_WmanIfCmnClassifierRuleIpSourceMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpSourceMask = _WmanIfCmnClassifierRuleIpSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 10),
    _WmanIfCmnClassifierRuleIpSourceMask_Type()
)
wmanIfCmnClassifierRuleIpSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpSourceMask.setStatus("current")
_WmanIfCmnClassifierRuleIpDestAddr_Type = InetAddress
_WmanIfCmnClassifierRuleIpDestAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleIpDestAddr = _WmanIfCmnClassifierRuleIpDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 11),
    _WmanIfCmnClassifierRuleIpDestAddr_Type()
)
wmanIfCmnClassifierRuleIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpDestAddr.setStatus("current")
_WmanIfCmnClassifierRuleIpDestMask_Type = InetAddress
_WmanIfCmnClassifierRuleIpDestMask_Object = MibTableColumn
wmanIfCmnClassifierRuleIpDestMask = _WmanIfCmnClassifierRuleIpDestMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 12),
    _WmanIfCmnClassifierRuleIpDestMask_Type()
)
wmanIfCmnClassifierRuleIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleIpDestMask.setStatus("current")


class _WmanIfCmnClassifierRuleSourcePortStart_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleSourcePortStart_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleSourcePortStart_Object = MibTableColumn
wmanIfCmnClassifierRuleSourcePortStart = _WmanIfCmnClassifierRuleSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 13),
    _WmanIfCmnClassifierRuleSourcePortStart_Type()
)
wmanIfCmnClassifierRuleSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourcePortStart.setStatus("current")


class _WmanIfCmnClassifierRuleSourcePortEnd_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleSourcePortEnd_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleSourcePortEnd_Object = MibTableColumn
wmanIfCmnClassifierRuleSourcePortEnd = _WmanIfCmnClassifierRuleSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 14),
    _WmanIfCmnClassifierRuleSourcePortEnd_Type()
)
wmanIfCmnClassifierRuleSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourcePortEnd.setStatus("current")


class _WmanIfCmnClassifierRuleDestPortStart_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleDestPortStart_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleDestPortStart_Object = MibTableColumn
wmanIfCmnClassifierRuleDestPortStart = _WmanIfCmnClassifierRuleDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 15),
    _WmanIfCmnClassifierRuleDestPortStart_Type()
)
wmanIfCmnClassifierRuleDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestPortStart.setStatus("current")


class _WmanIfCmnClassifierRuleDestPortEnd_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleDestPortEnd_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleDestPortEnd_Object = MibTableColumn
wmanIfCmnClassifierRuleDestPortEnd = _WmanIfCmnClassifierRuleDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 16),
    _WmanIfCmnClassifierRuleDestPortEnd_Type()
)
wmanIfCmnClassifierRuleDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestPortEnd.setStatus("current")
_WmanIfCmnClassifierRuleDestMacAddr_Type = MacAddress
_WmanIfCmnClassifierRuleDestMacAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleDestMacAddr = _WmanIfCmnClassifierRuleDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 17),
    _WmanIfCmnClassifierRuleDestMacAddr_Type()
)
wmanIfCmnClassifierRuleDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestMacAddr.setStatus("current")
_WmanIfCmnClassifierRuleDestMacMask_Type = MacAddress
_WmanIfCmnClassifierRuleDestMacMask_Object = MibTableColumn
wmanIfCmnClassifierRuleDestMacMask = _WmanIfCmnClassifierRuleDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 18),
    _WmanIfCmnClassifierRuleDestMacMask_Type()
)
wmanIfCmnClassifierRuleDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleDestMacMask.setStatus("current")
_WmanIfCmnClassifierRuleSourceMacAddr_Type = MacAddress
_WmanIfCmnClassifierRuleSourceMacAddr_Object = MibTableColumn
wmanIfCmnClassifierRuleSourceMacAddr = _WmanIfCmnClassifierRuleSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 19),
    _WmanIfCmnClassifierRuleSourceMacAddr_Type()
)
wmanIfCmnClassifierRuleSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourceMacAddr.setStatus("current")
_WmanIfCmnClassifierRuleSourceMacMask_Type = MacAddress
_WmanIfCmnClassifierRuleSourceMacMask_Object = MibTableColumn
wmanIfCmnClassifierRuleSourceMacMask = _WmanIfCmnClassifierRuleSourceMacMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 20),
    _WmanIfCmnClassifierRuleSourceMacMask_Type()
)
wmanIfCmnClassifierRuleSourceMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleSourceMacMask.setStatus("current")


class _WmanIfCmnClassifierRuleEnetProtocolType_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleEnetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ethertype", 1),
          ("dsap", 2))
    )


_WmanIfCmnClassifierRuleEnetProtocolType_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleEnetProtocolType_Object = MibTableColumn
wmanIfCmnClassifierRuleEnetProtocolType = _WmanIfCmnClassifierRuleEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 21),
    _WmanIfCmnClassifierRuleEnetProtocolType_Type()
)
wmanIfCmnClassifierRuleEnetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEnetProtocolType.setStatus("current")


class _WmanIfCmnClassifierRuleEnetProtocol_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnClassifierRuleEnetProtocol_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleEnetProtocol_Object = MibTableColumn
wmanIfCmnClassifierRuleEnetProtocol = _WmanIfCmnClassifierRuleEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 22),
    _WmanIfCmnClassifierRuleEnetProtocol_Type()
)
wmanIfCmnClassifierRuleEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleEnetProtocol.setStatus("current")


class _WmanIfCmnClassifierRuleUserPriLow_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfCmnClassifierRuleUserPriLow_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleUserPriLow_Object = MibTableColumn
wmanIfCmnClassifierRuleUserPriLow = _WmanIfCmnClassifierRuleUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 23),
    _WmanIfCmnClassifierRuleUserPriLow_Type()
)
wmanIfCmnClassifierRuleUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleUserPriLow.setStatus("current")


class _WmanIfCmnClassifierRuleUserPriHigh_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WmanIfCmnClassifierRuleUserPriHigh_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleUserPriHigh_Object = MibTableColumn
wmanIfCmnClassifierRuleUserPriHigh = _WmanIfCmnClassifierRuleUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 24),
    _WmanIfCmnClassifierRuleUserPriHigh_Type()
)
wmanIfCmnClassifierRuleUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleUserPriHigh.setStatus("current")


class _WmanIfCmnClassifierRuleVlanId_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WmanIfCmnClassifierRuleVlanId_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleVlanId_Object = MibTableColumn
wmanIfCmnClassifierRuleVlanId = _WmanIfCmnClassifierRuleVlanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 25),
    _WmanIfCmnClassifierRuleVlanId_Type()
)
wmanIfCmnClassifierRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleVlanId.setStatus("current")


class _WmanIfCmnClassifierRuleState_Type(Integer32):
    """Custom type wmanIfCmnClassifierRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WmanIfCmnClassifierRuleState_Type.__name__ = "Integer32"
_WmanIfCmnClassifierRuleState_Object = MibTableColumn
wmanIfCmnClassifierRuleState = _WmanIfCmnClassifierRuleState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 26),
    _WmanIfCmnClassifierRuleState_Type()
)
wmanIfCmnClassifierRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleState.setStatus("current")
_WmanIfCmnClassifierRulePkts_Type = Counter64
_WmanIfCmnClassifierRulePkts_Object = MibTableColumn
wmanIfCmnClassifierRulePkts = _WmanIfCmnClassifierRulePkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 27),
    _WmanIfCmnClassifierRulePkts_Type()
)
wmanIfCmnClassifierRulePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRulePkts.setStatus("current")
_WmanIfCmnClassifierRuleBitMap_Type = WmanIfClassifierBitMap
_WmanIfCmnClassifierRuleBitMap_Object = MibTableColumn
wmanIfCmnClassifierRuleBitMap = _WmanIfCmnClassifierRuleBitMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 1, 1, 1, 28),
    _WmanIfCmnClassifierRuleBitMap_Type()
)
wmanIfCmnClassifierRuleBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnClassifierRuleBitMap.setStatus("current")
_WmanIfCmnCps_ObjectIdentity = ObjectIdentity
wmanIfCmnCps = _WmanIfCmnCps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2)
)
_WmanIfCmnCpsServiceFlowTable_Object = MibTable
wmanIfCmnCpsServiceFlowTable = _WmanIfCmnCpsServiceFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnCpsServiceFlowTable.setStatus("deprecated")
_WmanIfCmnCpsServiceFlowEntry_Object = MibTableRow
wmanIfCmnCpsServiceFlowEntry = _WmanIfCmnCpsServiceFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1)
)
wmanIfCmnCpsServiceFlowEntry.setIndexNames(
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnCpsSfId"),
)
if mibBuilder.loadTexts:
    wmanIfCmnCpsServiceFlowEntry.setStatus("deprecated")


class _WmanIfCmnCpsSfId_Type(Unsigned32):
    """Custom type wmanIfCmnCpsSfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnCpsSfId_Type.__name__ = "Unsigned32"
_WmanIfCmnCpsSfId_Object = MibTableColumn
wmanIfCmnCpsSfId = _WmanIfCmnCpsSfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 1),
    _WmanIfCmnCpsSfId_Type()
)
wmanIfCmnCpsSfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfId.setStatus("deprecated")
_WmanIfCmnCpsSfCid_Type = Integer32
_WmanIfCmnCpsSfCid_Object = MibTableColumn
wmanIfCmnCpsSfCid = _WmanIfCmnCpsSfCid_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 2),
    _WmanIfCmnCpsSfCid_Type()
)
wmanIfCmnCpsSfCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfCid.setStatus("deprecated")


class _WmanIfCmnCpsSfDirection_Type(Integer32):
    """Custom type wmanIfCmnCpsSfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_WmanIfCmnCpsSfDirection_Type.__name__ = "Integer32"
_WmanIfCmnCpsSfDirection_Object = MibTableColumn
wmanIfCmnCpsSfDirection = _WmanIfCmnCpsSfDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 3),
    _WmanIfCmnCpsSfDirection_Type()
)
wmanIfCmnCpsSfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfDirection.setStatus("deprecated")


class _WmanIfCmnCpsSfState_Type(Integer32):
    """Custom type wmanIfCmnCpsSfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provisioned", 1),
          ("admitted", 2),
          ("active", 3))
    )


_WmanIfCmnCpsSfState_Type.__name__ = "Integer32"
_WmanIfCmnCpsSfState_Object = MibTableColumn
wmanIfCmnCpsSfState = _WmanIfCmnCpsSfState_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 4),
    _WmanIfCmnCpsSfState_Type()
)
wmanIfCmnCpsSfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfState.setStatus("deprecated")
_WmanIfCmnCpsServiceClassName_Type = DisplayString
_WmanIfCmnCpsServiceClassName_Object = MibTableColumn
wmanIfCmnCpsServiceClassName = _WmanIfCmnCpsServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 5),
    _WmanIfCmnCpsServiceClassName_Type()
)
wmanIfCmnCpsServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsServiceClassName.setStatus("deprecated")
_WmanIfCmnCpsTrafficPriority_Type = Integer32
_WmanIfCmnCpsTrafficPriority_Object = MibTableColumn
wmanIfCmnCpsTrafficPriority = _WmanIfCmnCpsTrafficPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 6),
    _WmanIfCmnCpsTrafficPriority_Type()
)
wmanIfCmnCpsTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsTrafficPriority.setStatus("deprecated")
_WmanIfCmnCpsMaxSustainedRate_Type = Integer32
_WmanIfCmnCpsMaxSustainedRate_Object = MibTableColumn
wmanIfCmnCpsMaxSustainedRate = _WmanIfCmnCpsMaxSustainedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 7),
    _WmanIfCmnCpsMaxSustainedRate_Type()
)
wmanIfCmnCpsMaxSustainedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxSustainedRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxSustainedRate.setUnits("bps")
_WmanIfCmnCpsMaxTrafficBurst_Type = Integer32
_WmanIfCmnCpsMaxTrafficBurst_Object = MibTableColumn
wmanIfCmnCpsMaxTrafficBurst = _WmanIfCmnCpsMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 8),
    _WmanIfCmnCpsMaxTrafficBurst_Type()
)
wmanIfCmnCpsMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxTrafficBurst.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxTrafficBurst.setUnits("byte")
_WmanIfCmnCpsMinReservedRate_Type = Integer32
_WmanIfCmnCpsMinReservedRate_Object = MibTableColumn
wmanIfCmnCpsMinReservedRate = _WmanIfCmnCpsMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 9),
    _WmanIfCmnCpsMinReservedRate_Type()
)
wmanIfCmnCpsMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinReservedRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinReservedRate.setUnits("byte")
_WmanIfCmnCpsToleratedJitter_Type = Integer32
_WmanIfCmnCpsToleratedJitter_Object = MibTableColumn
wmanIfCmnCpsToleratedJitter = _WmanIfCmnCpsToleratedJitter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 10),
    _WmanIfCmnCpsToleratedJitter_Type()
)
wmanIfCmnCpsToleratedJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsToleratedJitter.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsToleratedJitter.setUnits("millisecond")
_WmanIfCmnCpsMaxLatency_Type = Integer32
_WmanIfCmnCpsMaxLatency_Object = MibTableColumn
wmanIfCmnCpsMaxLatency = _WmanIfCmnCpsMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 11),
    _WmanIfCmnCpsMaxLatency_Type()
)
wmanIfCmnCpsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxLatency.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMaxLatency.setUnits("millisecond")


class _WmanIfCmnCpsFixedVsVariableSduInd_Type(Integer32):
    """Custom type wmanIfCmnCpsFixedVsVariableSduInd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("variableLengthSdu", 0),
          ("fixedLengthSdu", 1))
    )


_WmanIfCmnCpsFixedVsVariableSduInd_Type.__name__ = "Integer32"
_WmanIfCmnCpsFixedVsVariableSduInd_Object = MibTableColumn
wmanIfCmnCpsFixedVsVariableSduInd = _WmanIfCmnCpsFixedVsVariableSduInd_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 12),
    _WmanIfCmnCpsFixedVsVariableSduInd_Type()
)
wmanIfCmnCpsFixedVsVariableSduInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsFixedVsVariableSduInd.setStatus("deprecated")


class _WmanIfCmnCpsSduSize_Type(Integer32):
    """Custom type wmanIfCmnCpsSduSize based on Integer32"""
    defaultValue = 49


_WmanIfCmnCpsSduSize_Type.__name__ = "Integer32"
_WmanIfCmnCpsSduSize_Object = MibTableColumn
wmanIfCmnCpsSduSize = _WmanIfCmnCpsSduSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 13),
    _WmanIfCmnCpsSduSize_Type()
)
wmanIfCmnCpsSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSduSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSduSize.setUnits("byte")


class _WmanIfCmnCpsSfSchedulingType_Type(WmanIfSfSchedulingType):
    """Custom type wmanIfCmnCpsSfSchedulingType based on WmanIfSfSchedulingType"""
    defaultValue = 2


_WmanIfCmnCpsSfSchedulingType_Type.__name__ = "WmanIfSfSchedulingType"
_WmanIfCmnCpsSfSchedulingType_Object = MibTableColumn
wmanIfCmnCpsSfSchedulingType = _WmanIfCmnCpsSfSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 14),
    _WmanIfCmnCpsSfSchedulingType_Type()
)
wmanIfCmnCpsSfSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsSfSchedulingType.setStatus("deprecated")
_WmanIfCmnCpsArqEnable_Type = TruthValue
_WmanIfCmnCpsArqEnable_Object = MibTableColumn
wmanIfCmnCpsArqEnable = _WmanIfCmnCpsArqEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 15),
    _WmanIfCmnCpsArqEnable_Type()
)
wmanIfCmnCpsArqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqEnable.setStatus("deprecated")


class _WmanIfCmnCpsArqWindowSize_Type(Integer32):
    """Custom type wmanIfCmnCpsArqWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WmanIfCmnCpsArqWindowSize_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqWindowSize_Object = MibTableColumn
wmanIfCmnCpsArqWindowSize = _WmanIfCmnCpsArqWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 16),
    _WmanIfCmnCpsArqWindowSize_Type()
)
wmanIfCmnCpsArqWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqWindowSize.setStatus("deprecated")


class _WmanIfCmnCpsArqFragmentLifetime_Type(Integer32):
    """Custom type wmanIfCmnCpsArqFragmentLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqFragmentLifetime_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqFragmentLifetime_Object = MibTableColumn
wmanIfCmnCpsArqFragmentLifetime = _WmanIfCmnCpsArqFragmentLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 17),
    _WmanIfCmnCpsArqFragmentLifetime_Type()
)
wmanIfCmnCpsArqFragmentLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqFragmentLifetime.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqFragmentLifetime.setUnits("10 us")


class _WmanIfCmnCpsArqSyncLossTimeout_Type(Integer32):
    """Custom type wmanIfCmnCpsArqSyncLossTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqSyncLossTimeout_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqSyncLossTimeout_Object = MibTableColumn
wmanIfCmnCpsArqSyncLossTimeout = _WmanIfCmnCpsArqSyncLossTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 18),
    _WmanIfCmnCpsArqSyncLossTimeout_Type()
)
wmanIfCmnCpsArqSyncLossTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqSyncLossTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqSyncLossTimeout.setUnits("10 us")
_WmanIfCmnCpsArqDeliverInOrder_Type = TruthValue
_WmanIfCmnCpsArqDeliverInOrder_Object = MibTableColumn
wmanIfCmnCpsArqDeliverInOrder = _WmanIfCmnCpsArqDeliverInOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 19),
    _WmanIfCmnCpsArqDeliverInOrder_Type()
)
wmanIfCmnCpsArqDeliverInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqDeliverInOrder.setStatus("deprecated")


class _WmanIfCmnCpsArqRxPurgeTimeout_Type(Integer32):
    """Custom type wmanIfCmnCpsArqRxPurgeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnCpsArqRxPurgeTimeout_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqRxPurgeTimeout_Object = MibTableColumn
wmanIfCmnCpsArqRxPurgeTimeout = _WmanIfCmnCpsArqRxPurgeTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 20),
    _WmanIfCmnCpsArqRxPurgeTimeout_Type()
)
wmanIfCmnCpsArqRxPurgeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqRxPurgeTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqRxPurgeTimeout.setUnits("10 us")


class _WmanIfCmnCpsArqBlockSize_Type(Integer32):
    """Custom type wmanIfCmnCpsArqBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2040),
    )


_WmanIfCmnCpsArqBlockSize_Type.__name__ = "Integer32"
_WmanIfCmnCpsArqBlockSize_Object = MibTableColumn
wmanIfCmnCpsArqBlockSize = _WmanIfCmnCpsArqBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 21),
    _WmanIfCmnCpsArqBlockSize_Type()
)
wmanIfCmnCpsArqBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsArqBlockSize.setUnits("byte")
_WmanIfCmnCpsMinRsvdTolerableRate_Type = Integer32
_WmanIfCmnCpsMinRsvdTolerableRate_Object = MibTableColumn
wmanIfCmnCpsMinRsvdTolerableRate = _WmanIfCmnCpsMinRsvdTolerableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 22),
    _WmanIfCmnCpsMinRsvdTolerableRate_Type()
)
wmanIfCmnCpsMinRsvdTolerableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinRsvdTolerableRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    wmanIfCmnCpsMinRsvdTolerableRate.setUnits("bps")


class _WmanIfCmnCpsReqTxPolicy_Type(Bits):
    """Custom type wmanIfCmnCpsReqTxPolicy based on Bits"""
    namedValues = NamedValues(
        *(("noBroadcastBwReq", 0),
          ("reserved1", 1),
          ("noPiggybackReq", 2),
          ("noFragmentData", 3),
          ("noPHS", 4),
          ("noSduPacking", 5),
          ("noCrc", 6),
          ("reserved2", 7))
    )

_WmanIfCmnCpsReqTxPolicy_Type.__name__ = "Bits"
_WmanIfCmnCpsReqTxPolicy_Object = MibTableColumn
wmanIfCmnCpsReqTxPolicy = _WmanIfCmnCpsReqTxPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 1, 1, 23),
    _WmanIfCmnCpsReqTxPolicy_Type()
)
wmanIfCmnCpsReqTxPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCpsReqTxPolicy.setStatus("deprecated")
_WmanIfCmnBsSsConfigurationTable_Object = MibTable
wmanIfCmnBsSsConfigurationTable = _WmanIfCmnBsSsConfigurationTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wmanIfCmnBsSsConfigurationTable.setStatus("current")
_WmanIfCmnBsSsConfigurationEntry_Object = MibTableRow
wmanIfCmnBsSsConfigurationEntry = _WmanIfCmnBsSsConfigurationEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1)
)
wmanIfCmnBsSsConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnBsSsConfigurationEntry.setStatus("current")


class _WmanIfCmnInvitedRangRetries_Type(Integer32):
    """Custom type wmanIfCmnInvitedRangRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65535),
    )


_WmanIfCmnInvitedRangRetries_Type.__name__ = "Integer32"
_WmanIfCmnInvitedRangRetries_Object = MibTableColumn
wmanIfCmnInvitedRangRetries = _WmanIfCmnInvitedRangRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 1),
    _WmanIfCmnInvitedRangRetries_Type()
)
wmanIfCmnInvitedRangRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnInvitedRangRetries.setStatus("current")


class _WmanIfCmnMinislotSize_Type(Integer32):
    """Custom type wmanIfCmnMinislotSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WmanIfCmnMinislotSize_Type.__name__ = "Integer32"
_WmanIfCmnMinislotSize_Object = MibTableColumn
wmanIfCmnMinislotSize = _WmanIfCmnMinislotSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 2),
    _WmanIfCmnMinislotSize_Type()
)
wmanIfCmnMinislotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnMinislotSize.setStatus("current")


class _WmanIfCmnDSxReqRetries_Type(Integer32):
    """Custom type wmanIfCmnDSxReqRetries based on Integer32"""
    defaultValue = 3


_WmanIfCmnDSxReqRetries_Type.__name__ = "Integer32"
_WmanIfCmnDSxReqRetries_Object = MibTableColumn
wmanIfCmnDSxReqRetries = _WmanIfCmnDSxReqRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 3),
    _WmanIfCmnDSxReqRetries_Type()
)
wmanIfCmnDSxReqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnDSxReqRetries.setStatus("current")


class _WmanIfCmnDSxRespRetries_Type(Integer32):
    """Custom type wmanIfCmnDSxRespRetries based on Integer32"""
    defaultValue = 3


_WmanIfCmnDSxRespRetries_Type.__name__ = "Integer32"
_WmanIfCmnDSxRespRetries_Object = MibTableColumn
wmanIfCmnDSxRespRetries = _WmanIfCmnDSxRespRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 4),
    _WmanIfCmnDSxRespRetries_Type()
)
wmanIfCmnDSxRespRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnDSxRespRetries.setStatus("current")


class _WmanIfCmnT7Timeout_Type(Integer32):
    """Custom type wmanIfCmnT7Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WmanIfCmnT7Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT7Timeout_Object = MibTableColumn
wmanIfCmnT7Timeout = _WmanIfCmnT7Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 5),
    _WmanIfCmnT7Timeout_Type()
)
wmanIfCmnT7Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT7Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT7Timeout.setUnits("milliseconds")


class _WmanIfCmnT8Timeout_Type(Integer32):
    """Custom type wmanIfCmnT8Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WmanIfCmnT8Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT8Timeout_Object = MibTableColumn
wmanIfCmnT8Timeout = _WmanIfCmnT8Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 6),
    _WmanIfCmnT8Timeout_Type()
)
wmanIfCmnT8Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT8Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT8Timeout.setUnits("milliseconds")


class _WmanIfCmnT10Timeout_Type(Integer32):
    """Custom type wmanIfCmnT10Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_WmanIfCmnT10Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT10Timeout_Object = MibTableColumn
wmanIfCmnT10Timeout = _WmanIfCmnT10Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 7),
    _WmanIfCmnT10Timeout_Type()
)
wmanIfCmnT10Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT10Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT10Timeout.setUnits("milliseconds")


class _WmanIfCmnT22Timeout_Type(Integer32):
    """Custom type wmanIfCmnT22Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WmanIfCmnT22Timeout_Type.__name__ = "Integer32"
_WmanIfCmnT22Timeout_Object = MibTableColumn
wmanIfCmnT22Timeout = _WmanIfCmnT22Timeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 2, 1, 8),
    _WmanIfCmnT22Timeout_Type()
)
wmanIfCmnT22Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnT22Timeout.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnT22Timeout.setUnits("milliseconds")
_WmanIfCmnSsStatCounter_ObjectIdentity = ObjectIdentity
wmanIfCmnSsStatCounter = _WmanIfCmnSsStatCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3)
)
_WmanIfCmnSsChMeasurementTable_Object = MibTable
wmanIfCmnSsChMeasurementTable = _WmanIfCmnSsChMeasurementTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnSsChMeasurementTable.setStatus("current")
_WmanIfCmnSsChMeasurementEntry_Object = MibTableRow
wmanIfCmnSsChMeasurementEntry = _WmanIfCmnSsChMeasurementEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1)
)
wmanIfCmnSsChMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnSsIdIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnHistogramIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnSsChMeasurementEntry.setStatus("current")


class _WmanIfCmnSsIdIndex_Type(Unsigned32):
    """Custom type wmanIfCmnSsIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnSsIdIndex_Type.__name__ = "Unsigned32"
_WmanIfCmnSsIdIndex_Object = MibTableColumn
wmanIfCmnSsIdIndex = _WmanIfCmnSsIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 1),
    _WmanIfCmnSsIdIndex_Type()
)
wmanIfCmnSsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnSsIdIndex.setStatus("current")


class _WmanIfCmnHistogramIndex_Type(Unsigned32):
    """Custom type wmanIfCmnHistogramIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnHistogramIndex_Type.__name__ = "Unsigned32"
_WmanIfCmnHistogramIndex_Object = MibTableColumn
wmanIfCmnHistogramIndex = _WmanIfCmnHistogramIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 2),
    _WmanIfCmnHistogramIndex_Type()
)
wmanIfCmnHistogramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnHistogramIndex.setStatus("current")
_WmanIfCmnChannelNumber_Type = Integer32
_WmanIfCmnChannelNumber_Object = MibTableColumn
wmanIfCmnChannelNumber = _WmanIfCmnChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 3),
    _WmanIfCmnChannelNumber_Type()
)
wmanIfCmnChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnChannelNumber.setStatus("current")
_WmanIfCmnStartFrame_Type = Integer32
_WmanIfCmnStartFrame_Object = MibTableColumn
wmanIfCmnStartFrame = _WmanIfCmnStartFrame_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 4),
    _WmanIfCmnStartFrame_Type()
)
wmanIfCmnStartFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnStartFrame.setStatus("current")
_WmanIfCmnDuration_Type = Integer32
_WmanIfCmnDuration_Object = MibTableColumn
wmanIfCmnDuration = _WmanIfCmnDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 5),
    _WmanIfCmnDuration_Type()
)
wmanIfCmnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnDuration.setStatus("current")


class _WmanIfCmnBasicReport_Type(Bits):
    """Custom type wmanIfCmnBasicReport based on Bits"""
    namedValues = NamedValues(
        *(("wirelessHuman", 0),
          ("unknownTransmission", 1),
          ("primaryUser", 2),
          ("channegNotMeasured", 3))
    )

_WmanIfCmnBasicReport_Type.__name__ = "Bits"
_WmanIfCmnBasicReport_Object = MibTableColumn
wmanIfCmnBasicReport = _WmanIfCmnBasicReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 6),
    _WmanIfCmnBasicReport_Type()
)
wmanIfCmnBasicReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnBasicReport.setStatus("current")
_WmanIfCmnMeanCinrReport_Type = Integer32
_WmanIfCmnMeanCinrReport_Object = MibTableColumn
wmanIfCmnMeanCinrReport = _WmanIfCmnMeanCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 7),
    _WmanIfCmnMeanCinrReport_Type()
)
wmanIfCmnMeanCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnMeanCinrReport.setStatus("current")
_WmanIfCmnStdDeviationCinrReport_Type = Integer32
_WmanIfCmnStdDeviationCinrReport_Object = MibTableColumn
wmanIfCmnStdDeviationCinrReport = _WmanIfCmnStdDeviationCinrReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 8),
    _WmanIfCmnStdDeviationCinrReport_Type()
)
wmanIfCmnStdDeviationCinrReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnStdDeviationCinrReport.setStatus("current")
_WmanIfCmnMeanRssiReport_Type = Integer32
_WmanIfCmnMeanRssiReport_Object = MibTableColumn
wmanIfCmnMeanRssiReport = _WmanIfCmnMeanRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 9),
    _WmanIfCmnMeanRssiReport_Type()
)
wmanIfCmnMeanRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnMeanRssiReport.setStatus("current")
_WmanIfCmnStdDeviationRssiReport_Type = Integer32
_WmanIfCmnStdDeviationRssiReport_Object = MibTableColumn
wmanIfCmnStdDeviationRssiReport = _WmanIfCmnStdDeviationRssiReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 1, 1, 10),
    _WmanIfCmnStdDeviationRssiReport_Type()
)
wmanIfCmnStdDeviationRssiReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnStdDeviationRssiReport.setStatus("current")
_WmanIfCmnSsFecCounterTable_Object = MibTable
wmanIfCmnSsFecCounterTable = _WmanIfCmnSsFecCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wmanIfCmnSsFecCounterTable.setStatus("current")
_WmanIfCmnSsFecCounterEntry_Object = MibTableRow
wmanIfCmnSsFecCounterEntry = _WmanIfCmnSsFecCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1)
)
wmanIfCmnSsFecCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnSsFecSsId"),
)
if mibBuilder.loadTexts:
    wmanIfCmnSsFecCounterEntry.setStatus("current")


class _WmanIfCmnSsFecSsId_Type(Unsigned32):
    """Custom type wmanIfCmnSsFecSsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WmanIfCmnSsFecSsId_Type.__name__ = "Unsigned32"
_WmanIfCmnSsFecSsId_Object = MibTableColumn
wmanIfCmnSsFecSsId = _WmanIfCmnSsFecSsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1, 1),
    _WmanIfCmnSsFecSsId_Type()
)
wmanIfCmnSsFecSsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecSsId.setStatus("current")
_WmanIfCmnSsFecCorrectedBytes_Type = Counter64
_WmanIfCmnSsFecCorrectedBytes_Object = MibTableColumn
wmanIfCmnSsFecCorrectedBytes = _WmanIfCmnSsFecCorrectedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1, 2),
    _WmanIfCmnSsFecCorrectedBytes_Type()
)
wmanIfCmnSsFecCorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecCorrectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecCorrectedBytes.setUnits("bytes")
_WmanIfCmnSsFecUncorrectedBytes_Type = Counter64
_WmanIfCmnSsFecUncorrectedBytes_Object = MibTableColumn
wmanIfCmnSsFecUncorrectedBytes = _WmanIfCmnSsFecUncorrectedBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1, 3),
    _WmanIfCmnSsFecUncorrectedBytes_Type()
)
wmanIfCmnSsFecUncorrectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecUncorrectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecUncorrectedBytes.setUnits("bytes")
_WmanIfCmnSsFecUncorrectedMacPdu_Type = Counter64
_WmanIfCmnSsFecUncorrectedMacPdu_Object = MibTableColumn
wmanIfCmnSsFecUncorrectedMacPdu = _WmanIfCmnSsFecUncorrectedMacPdu_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1, 4),
    _WmanIfCmnSsFecUncorrectedMacPdu_Type()
)
wmanIfCmnSsFecUncorrectedMacPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecUncorrectedMacPdu.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecUncorrectedMacPdu.setUnits("MAC PDU")


class _WmanIfCmnSsFecResetCounter_Type(Integer32):
    """Custom type wmanIfCmnSsFecResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("resetCounter", 1))
    )


_WmanIfCmnSsFecResetCounter_Type.__name__ = "Integer32"
_WmanIfCmnSsFecResetCounter_Object = MibTableColumn
wmanIfCmnSsFecResetCounter = _WmanIfCmnSsFecResetCounter_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 2, 3, 2, 1, 5),
    _WmanIfCmnSsFecResetCounter_Type()
)
wmanIfCmnSsFecResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnSsFecResetCounter.setStatus("current")
_WmanIfCmnPkmObjects_ObjectIdentity = ObjectIdentity
wmanIfCmnPkmObjects = _WmanIfCmnPkmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3)
)
_WmanIfCmnCryptoSuiteTable_Object = MibTable
wmanIfCmnCryptoSuiteTable = _WmanIfCmnCryptoSuiteTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteTable.setStatus("current")
_WmanIfCmnCryptoSuiteEntry_Object = MibTableRow
wmanIfCmnCryptoSuiteEntry = _WmanIfCmnCryptoSuiteEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1)
)
wmanIfCmnCryptoSuiteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnCryptoSuiteIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteEntry.setStatus("current")


class _WmanIfCmnCryptoSuiteIndex_Type(Integer32):
    """Custom type wmanIfCmnCryptoSuiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WmanIfCmnCryptoSuiteIndex_Type.__name__ = "Integer32"
_WmanIfCmnCryptoSuiteIndex_Object = MibTableColumn
wmanIfCmnCryptoSuiteIndex = _WmanIfCmnCryptoSuiteIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 1),
    _WmanIfCmnCryptoSuiteIndex_Type()
)
wmanIfCmnCryptoSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteIndex.setStatus("current")


class _WmanIfCmnCryptoSuiteDataEncryptAlg_Type(Integer32):
    """Custom type wmanIfCmnCryptoSuiteDataEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des56CbcMode", 1),
          ("aesCcmMode", 2))
    )


_WmanIfCmnCryptoSuiteDataEncryptAlg_Type.__name__ = "Integer32"
_WmanIfCmnCryptoSuiteDataEncryptAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteDataEncryptAlg = _WmanIfCmnCryptoSuiteDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 2),
    _WmanIfCmnCryptoSuiteDataEncryptAlg_Type()
)
wmanIfCmnCryptoSuiteDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteDataEncryptAlg.setStatus("current")


class _WmanIfCmnCryptoSuiteDataAuthentAlg_Type(Integer32):
    """Custom type wmanIfCmnCryptoSuiteDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_WmanIfCmnCryptoSuiteDataAuthentAlg_Type.__name__ = "Integer32"
_WmanIfCmnCryptoSuiteDataAuthentAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteDataAuthentAlg = _WmanIfCmnCryptoSuiteDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 3),
    _WmanIfCmnCryptoSuiteDataAuthentAlg_Type()
)
wmanIfCmnCryptoSuiteDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteDataAuthentAlg.setStatus("current")


class _WmanIfCmnCryptoSuiteTEKEncryptAlg_Type(Integer32):
    """Custom type wmanIfCmnCryptoSuiteTEKEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tripleDES128Key", 1),
          ("rsa1024Key", 2),
          ("aes128Key", 3))
    )


_WmanIfCmnCryptoSuiteTEKEncryptAlg_Type.__name__ = "Integer32"
_WmanIfCmnCryptoSuiteTEKEncryptAlg_Object = MibTableColumn
wmanIfCmnCryptoSuiteTEKEncryptAlg = _WmanIfCmnCryptoSuiteTEKEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 3, 1, 1, 4),
    _WmanIfCmnCryptoSuiteTEKEncryptAlg_Type()
)
wmanIfCmnCryptoSuiteTEKEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmanIfCmnCryptoSuiteTEKEncryptAlg.setStatus("current")
_WmanIfCmnOfdmPhy_ObjectIdentity = ObjectIdentity
wmanIfCmnOfdmPhy = _WmanIfCmnOfdmPhy_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4)
)
_WmanIfCmnOfdmUplinkChannelTable_Object = MibTable
wmanIfCmnOfdmUplinkChannelTable = _WmanIfCmnOfdmUplinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkChannelTable.setStatus("current")
_WmanIfCmnOfdmUplinkChannelEntry_Object = MibTableRow
wmanIfCmnOfdmUplinkChannelEntry = _WmanIfCmnOfdmUplinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1)
)
wmanIfCmnOfdmUplinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkChannelEntry.setStatus("current")


class _WmanIfCmnOfdmCtBasedResvTimeout_Type(Integer32):
    """Custom type wmanIfCmnOfdmCtBasedResvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfCmnOfdmCtBasedResvTimeout_Type.__name__ = "Integer32"
_WmanIfCmnOfdmCtBasedResvTimeout_Object = MibTableColumn
wmanIfCmnOfdmCtBasedResvTimeout = _WmanIfCmnOfdmCtBasedResvTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 1),
    _WmanIfCmnOfdmCtBasedResvTimeout_Type()
)
wmanIfCmnOfdmCtBasedResvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmCtBasedResvTimeout.setStatus("current")


class _WmanIfCmnOfdmBwReqOppSize_Type(Integer32):
    """Custom type wmanIfCmnOfdmBwReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfCmnOfdmBwReqOppSize_Type.__name__ = "Integer32"
_WmanIfCmnOfdmBwReqOppSize_Object = MibTableColumn
wmanIfCmnOfdmBwReqOppSize = _WmanIfCmnOfdmBwReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 2),
    _WmanIfCmnOfdmBwReqOppSize_Type()
)
wmanIfCmnOfdmBwReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmBwReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmBwReqOppSize.setUnits("PS")


class _WmanIfCmnOfdmRangReqOppSize_Type(Integer32):
    """Custom type wmanIfCmnOfdmRangReqOppSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WmanIfCmnOfdmRangReqOppSize_Type.__name__ = "Integer32"
_WmanIfCmnOfdmRangReqOppSize_Object = MibTableColumn
wmanIfCmnOfdmRangReqOppSize = _WmanIfCmnOfdmRangReqOppSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 3),
    _WmanIfCmnOfdmRangReqOppSize_Type()
)
wmanIfCmnOfdmRangReqOppSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmRangReqOppSize.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmRangReqOppSize.setUnits("PS")
_WmanIfCmnOfdmUplinkCenterFreq_Type = Integer32
_WmanIfCmnOfdmUplinkCenterFreq_Object = MibTableColumn
wmanIfCmnOfdmUplinkCenterFreq = _WmanIfCmnOfdmUplinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 4),
    _WmanIfCmnOfdmUplinkCenterFreq_Type()
)
wmanIfCmnOfdmUplinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkCenterFreq.setUnits("KHz")


class _WmanIfCmnOfdmSubChReqRegionFull_Type(Integer32):
    """Custom type wmanIfCmnOfdmSubChReqRegionFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnOfdmSubChReqRegionFull_Type.__name__ = "Integer32"
_WmanIfCmnOfdmSubChReqRegionFull_Object = MibTableColumn
wmanIfCmnOfdmSubChReqRegionFull = _WmanIfCmnOfdmSubChReqRegionFull_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 5),
    _WmanIfCmnOfdmSubChReqRegionFull_Type()
)
wmanIfCmnOfdmSubChReqRegionFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmSubChReqRegionFull.setStatus("current")


class _WmanIfCmnOfdmSubChFocusCtCode_Type(Integer32):
    """Custom type wmanIfCmnOfdmSubChFocusCtCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WmanIfCmnOfdmSubChFocusCtCode_Type.__name__ = "Integer32"
_WmanIfCmnOfdmSubChFocusCtCode_Object = MibTableColumn
wmanIfCmnOfdmSubChFocusCtCode = _WmanIfCmnOfdmSubChFocusCtCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 1, 1, 6),
    _WmanIfCmnOfdmSubChFocusCtCode_Type()
)
wmanIfCmnOfdmSubChFocusCtCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmSubChFocusCtCode.setStatus("current")
_WmanIfCmnOfdmDownlinkChannelTable_Object = MibTable
wmanIfCmnOfdmDownlinkChannelTable = _WmanIfCmnOfdmDownlinkChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkChannelTable.setStatus("current")
_WmanIfCmnOfdmDownlinkChannelEntry_Object = MibTableRow
wmanIfCmnOfdmDownlinkChannelEntry = _WmanIfCmnOfdmDownlinkChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1)
)
wmanIfCmnOfdmDownlinkChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkChannelEntry.setStatus("current")


class _WmanIfCmnOfdmBsEIRP_Type(Integer32):
    """Custom type wmanIfCmnOfdmBsEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIfCmnOfdmBsEIRP_Type.__name__ = "Integer32"
_WmanIfCmnOfdmBsEIRP_Object = MibTableColumn
wmanIfCmnOfdmBsEIRP = _WmanIfCmnOfdmBsEIRP_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 1),
    _WmanIfCmnOfdmBsEIRP_Type()
)
wmanIfCmnOfdmBsEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmBsEIRP.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmBsEIRP.setUnits("dbM")


class _WmanIfCmnOfdmChannelNumber_Type(Integer32):
    """Custom type wmanIfCmnOfdmChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WmanIfCmnOfdmChannelNumber_Type.__name__ = "Integer32"
_WmanIfCmnOfdmChannelNumber_Object = MibTableColumn
wmanIfCmnOfdmChannelNumber = _WmanIfCmnOfdmChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 2),
    _WmanIfCmnOfdmChannelNumber_Type()
)
wmanIfCmnOfdmChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmChannelNumber.setStatus("current")


class _WmanIfCmnOfdmTTG_Type(Integer32):
    """Custom type wmanIfCmnOfdmTTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmanIfCmnOfdmTTG_Type.__name__ = "Integer32"
_WmanIfCmnOfdmTTG_Object = MibTableColumn
wmanIfCmnOfdmTTG = _WmanIfCmnOfdmTTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 3),
    _WmanIfCmnOfdmTTG_Type()
)
wmanIfCmnOfdmTTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmTTG.setStatus("current")


class _WmanIfCmnOfdmRTG_Type(Integer32):
    """Custom type wmanIfCmnOfdmRTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnOfdmRTG_Type.__name__ = "Integer32"
_WmanIfCmnOfdmRTG_Object = MibTableColumn
wmanIfCmnOfdmRTG = _WmanIfCmnOfdmRTG_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 4),
    _WmanIfCmnOfdmRTG_Type()
)
wmanIfCmnOfdmRTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmRTG.setStatus("current")


class _WmanIfCmnOfdmInitRngMaxRSS_Type(Integer32):
    """Custom type wmanIfCmnOfdmInitRngMaxRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_WmanIfCmnOfdmInitRngMaxRSS_Type.__name__ = "Integer32"
_WmanIfCmnOfdmInitRngMaxRSS_Object = MibTableColumn
wmanIfCmnOfdmInitRngMaxRSS = _WmanIfCmnOfdmInitRngMaxRSS_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 5),
    _WmanIfCmnOfdmInitRngMaxRSS_Type()
)
wmanIfCmnOfdmInitRngMaxRSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmInitRngMaxRSS.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmInitRngMaxRSS.setUnits("dbM")


class _WmanIfCmnOfdmChSwitchFrameNmr_Type(Integer32):
    """Custom type wmanIfCmnOfdmChSwitchFrameNmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_WmanIfCmnOfdmChSwitchFrameNmr_Type.__name__ = "Integer32"
_WmanIfCmnOfdmChSwitchFrameNmr_Object = MibTableColumn
wmanIfCmnOfdmChSwitchFrameNmr = _WmanIfCmnOfdmChSwitchFrameNmr_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 6),
    _WmanIfCmnOfdmChSwitchFrameNmr_Type()
)
wmanIfCmnOfdmChSwitchFrameNmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmChSwitchFrameNmr.setStatus("current")
_WmanIfCmnOfdmDownlinkCenterFreq_Type = Integer32
_WmanIfCmnOfdmDownlinkCenterFreq_Object = MibTableColumn
wmanIfCmnOfdmDownlinkCenterFreq = _WmanIfCmnOfdmDownlinkCenterFreq_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 7),
    _WmanIfCmnOfdmDownlinkCenterFreq_Type()
)
wmanIfCmnOfdmDownlinkCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkCenterFreq.setUnits("KHz")


class _WmanIfCmnOfdmBsId_Type(OctetString):
    """Custom type wmanIfCmnOfdmBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_WmanIfCmnOfdmBsId_Type.__name__ = "OctetString"
_WmanIfCmnOfdmBsId_Object = MibTableColumn
wmanIfCmnOfdmBsId = _WmanIfCmnOfdmBsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 8),
    _WmanIfCmnOfdmBsId_Type()
)
wmanIfCmnOfdmBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmBsId.setStatus("current")


class _WmanIfCmnOfdmMacVersion_Type(Integer32):
    """Custom type wmanIfCmnOfdmMacVersion based on Integer32"""
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
        *(("ieee802Dot16-2001", 1),
          ("ieee802Dot16c-2002", 2),
          ("ieee802Dot16a-2003", 3),
          ("ieee802Dot16-2004", 4),
          ("ieee802Dot16-2004Cor1", 5))
    )


_WmanIfCmnOfdmMacVersion_Type.__name__ = "Integer32"
_WmanIfCmnOfdmMacVersion_Object = MibTableColumn
wmanIfCmnOfdmMacVersion = _WmanIfCmnOfdmMacVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 9),
    _WmanIfCmnOfdmMacVersion_Type()
)
wmanIfCmnOfdmMacVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmMacVersion.setStatus("current")


class _WmanIfCmnOfdmFrameDurationCode_Type(Integer32):
    """Custom type wmanIfCmnOfdmFrameDurationCode based on Integer32"""
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
        *(("duration2dot5ms", 0),
          ("duration4ms", 1),
          ("duration5ms", 2),
          ("duration8ms", 3),
          ("duration10ms", 4),
          ("duration12dot5ms", 5),
          ("duration20ms", 6))
    )


_WmanIfCmnOfdmFrameDurationCode_Type.__name__ = "Integer32"
_WmanIfCmnOfdmFrameDurationCode_Object = MibTableColumn
wmanIfCmnOfdmFrameDurationCode = _WmanIfCmnOfdmFrameDurationCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 10),
    _WmanIfCmnOfdmFrameDurationCode_Type()
)
wmanIfCmnOfdmFrameDurationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmFrameDurationCode.setStatus("current")


class _WmanIfCmnOfdmFrameNumber_Type(Integer32):
    """Custom type wmanIfCmnOfdmFrameNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_WmanIfCmnOfdmFrameNumber_Type.__name__ = "Integer32"
_WmanIfCmnOfdmFrameNumber_Object = MibTableColumn
wmanIfCmnOfdmFrameNumber = _WmanIfCmnOfdmFrameNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 2, 1, 11),
    _WmanIfCmnOfdmFrameNumber_Type()
)
wmanIfCmnOfdmFrameNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmFrameNumber.setStatus("current")
_WmanIfCmnOfdmUcdBurstProfileTable_Object = MibTable
wmanIfCmnOfdmUcdBurstProfileTable = _WmanIfCmnOfdmUcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUcdBurstProfileTable.setStatus("current")
_WmanIfCmnOfdmUcdBurstProfileEntry_Object = MibTableRow
wmanIfCmnOfdmUcdBurstProfileEntry = _WmanIfCmnOfdmUcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1)
)
wmanIfCmnOfdmUcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnOfdmUiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUcdBurstProfileEntry.setStatus("current")


class _WmanIfCmnOfdmUiucIndex_Type(Integer32):
    """Custom type wmanIfCmnOfdmUiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_WmanIfCmnOfdmUiucIndex_Type.__name__ = "Integer32"
_WmanIfCmnOfdmUiucIndex_Object = MibTableColumn
wmanIfCmnOfdmUiucIndex = _WmanIfCmnOfdmUiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1, 1),
    _WmanIfCmnOfdmUiucIndex_Type()
)
wmanIfCmnOfdmUiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUiucIndex.setStatus("current")
_WmanIfCmnOfdmUplinkFrequency_Type = Integer32
_WmanIfCmnOfdmUplinkFrequency_Object = MibTableColumn
wmanIfCmnOfdmUplinkFrequency = _WmanIfCmnOfdmUplinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1, 2),
    _WmanIfCmnOfdmUplinkFrequency_Type()
)
wmanIfCmnOfdmUplinkFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUplinkFrequency.setUnits("KHz")
_WmanIfCmnOfdmUcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfCmnOfdmUcdFecCodeType_Object = MibTableColumn
wmanIfCmnOfdmUcdFecCodeType = _WmanIfCmnOfdmUcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1, 3),
    _WmanIfCmnOfdmUcdFecCodeType_Type()
)
wmanIfCmnOfdmUcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUcdFecCodeType.setStatus("current")
_WmanIfCmnOfdmFocusCtPowerBoost_Type = Integer32
_WmanIfCmnOfdmFocusCtPowerBoost_Object = MibTableColumn
wmanIfCmnOfdmFocusCtPowerBoost = _WmanIfCmnOfdmFocusCtPowerBoost_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1, 4),
    _WmanIfCmnOfdmFocusCtPowerBoost_Type()
)
wmanIfCmnOfdmFocusCtPowerBoost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmFocusCtPowerBoost.setStatus("current")
_WmanIfCmnOfdmUcdBurstProfileRowStatus_Type = RowStatus
_WmanIfCmnOfdmUcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfCmnOfdmUcdBurstProfileRowStatus = _WmanIfCmnOfdmUcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 3, 1, 5),
    _WmanIfCmnOfdmUcdBurstProfileRowStatus_Type()
)
wmanIfCmnOfdmUcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmUcdBurstProfileRowStatus.setStatus("current")
_WmanIfCmnOfdmDcdBurstProfileTable_Object = MibTable
wmanIfCmnOfdmDcdBurstProfileTable = _WmanIfCmnOfdmDcdBurstProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDcdBurstProfileTable.setStatus("current")
_WmanIfCmnOfdmDcdBurstProfileEntry_Object = MibTableRow
wmanIfCmnOfdmDcdBurstProfileEntry = _WmanIfCmnOfdmDcdBurstProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1)
)
wmanIfCmnOfdmDcdBurstProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WMAN-IF-ASDRAFT1-MIB", "wmanIfCmnOfdmDiucIndex"),
)
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDcdBurstProfileEntry.setStatus("current")


class _WmanIfCmnOfdmDiucIndex_Type(Integer32):
    """Custom type wmanIfCmnOfdmDiucIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_WmanIfCmnOfdmDiucIndex_Type.__name__ = "Integer32"
_WmanIfCmnOfdmDiucIndex_Object = MibTableColumn
wmanIfCmnOfdmDiucIndex = _WmanIfCmnOfdmDiucIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 1),
    _WmanIfCmnOfdmDiucIndex_Type()
)
wmanIfCmnOfdmDiucIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDiucIndex.setStatus("current")
_WmanIfCmnOfdmDownlinkFrequency_Type = Integer32
_WmanIfCmnOfdmDownlinkFrequency_Object = MibTableColumn
wmanIfCmnOfdmDownlinkFrequency = _WmanIfCmnOfdmDownlinkFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 2),
    _WmanIfCmnOfdmDownlinkFrequency_Type()
)
wmanIfCmnOfdmDownlinkFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDownlinkFrequency.setUnits("KHz")
_WmanIfCmnOfdmDcdFecCodeType_Type = WmanIfOfdmFecCodeType
_WmanIfCmnOfdmDcdFecCodeType_Object = MibTableColumn
wmanIfCmnOfdmDcdFecCodeType = _WmanIfCmnOfdmDcdFecCodeType_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 3),
    _WmanIfCmnOfdmDcdFecCodeType_Type()
)
wmanIfCmnOfdmDcdFecCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDcdFecCodeType.setStatus("current")


class _WmanIfCmnOfdmDiucMandatoryExitThresh_Type(Integer32):
    """Custom type wmanIfCmnOfdmDiucMandatoryExitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnOfdmDiucMandatoryExitThresh_Type.__name__ = "Integer32"
_WmanIfCmnOfdmDiucMandatoryExitThresh_Object = MibTableColumn
wmanIfCmnOfdmDiucMandatoryExitThresh = _WmanIfCmnOfdmDiucMandatoryExitThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 4),
    _WmanIfCmnOfdmDiucMandatoryExitThresh_Type()
)
wmanIfCmnOfdmDiucMandatoryExitThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDiucMandatoryExitThresh.setStatus("current")


class _WmanIfCmnOfdmDiucMinEntryThresh_Type(Integer32):
    """Custom type wmanIfCmnOfdmDiucMinEntryThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmanIfCmnOfdmDiucMinEntryThresh_Type.__name__ = "Integer32"
_WmanIfCmnOfdmDiucMinEntryThresh_Object = MibTableColumn
wmanIfCmnOfdmDiucMinEntryThresh = _WmanIfCmnOfdmDiucMinEntryThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 5),
    _WmanIfCmnOfdmDiucMinEntryThresh_Type()
)
wmanIfCmnOfdmDiucMinEntryThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDiucMinEntryThresh.setStatus("current")


class _WmanIfCmnOfdmTcsEnable_Type(Integer32):
    """Custom type wmanIfCmnOfdmTcsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcsDisabled", 0),
          ("tcsEnabled", 1))
    )


_WmanIfCmnOfdmTcsEnable_Type.__name__ = "Integer32"
_WmanIfCmnOfdmTcsEnable_Object = MibTableColumn
wmanIfCmnOfdmTcsEnable = _WmanIfCmnOfdmTcsEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 6),
    _WmanIfCmnOfdmTcsEnable_Type()
)
wmanIfCmnOfdmTcsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmTcsEnable.setStatus("current")
_WmanIfCmnOfdmDcdBurstProfileRowStatus_Type = RowStatus
_WmanIfCmnOfdmDcdBurstProfileRowStatus_Object = MibTableColumn
wmanIfCmnOfdmDcdBurstProfileRowStatus = _WmanIfCmnOfdmDcdBurstProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 3, 4, 4, 1, 7),
    _WmanIfCmnOfdmDcdBurstProfileRowStatus_Type()
)
wmanIfCmnOfdmDcdBurstProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmanIfCmnOfdmDcdBurstProfileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

wmanBsSsStatusNotificationTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 3)
)
wmanBsSsStatusNotificationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTrapSsId"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsNotMacAddr"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsStatusValue"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanBsSsStatusNotificationTrap.setStatus(
        "current"
    )

wmanBsSsDynamicServiceFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 4)
)
wmanBsSsDynamicServiceFailTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTrapSsId"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsNotMacAddr"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsDynamicServiceType"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsDynamicServiceFailReason"))
)
if mibBuilder.loadTexts:
    wmanBsSsDynamicServiceFailTrap.setStatus(
        "current"
    )

wmanBsSsRssiStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 5)
)
wmanBsSsRssiStatusChangeTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTrapSsId"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsNotMacAddr"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsRssiStatus"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanBsSsRssiStatusChangeTrap.setStatus(
        "current"
    )

wmanBsSsBPKMFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 6)
)
wmanBsSsBPKMFailTrap.setObjects(
    ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsSsNotMacAddr")
)
if mibBuilder.loadTexts:
    wmanBsSsBPKMFailTrap.setStatus(
        "current"
    )

wmanBsPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 8)
)
wmanBsPowerStatusChangeTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsPowerStatus"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsPowerStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanBsPowerStatusChangeTrap.setStatus(
        "current"
    )

wmanBsFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 9)
)
wmanBsFanStatusTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsFanStatus"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsFanStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanBsFanStatusTrap.setStatus(
        "current"
    )

wmanBsTemperatureChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 1, 4, 1, 10)
)
wmanBsTemperatureChangeTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTemperatureStatus"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfBsTemperatureStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanBsTemperatureChangeTrap.setStatus(
        "current"
    )

wmanSsTLVUnknownTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 1)
)
wmanSsTLVUnknownTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsUnknownTlv"))
)
if mibBuilder.loadTexts:
    wmanSsTLVUnknownTrap.setStatus(
        "current"
    )

wmanSsDynamicServiceFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 2)
)
wmanSsDynamicServiceFailTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsDynamicServiceType"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsDynamicServiceFailReason"))
)
if mibBuilder.loadTexts:
    wmanSsDynamicServiceFailTrap.setStatus(
        "current"
    )

wmanSsDHCPSuccessTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 3)
)
wmanSsDHCPSuccessTrap.setObjects(
    ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsMacAddress")
)
if mibBuilder.loadTexts:
    wmanSsDHCPSuccessTrap.setStatus(
        "current"
    )

wmanSsRssiStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 184, 1, 2, 3, 1, 4)
)
wmanSsRssiStatusChangeTrap.setObjects(
      *(("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsMacAddress"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsRssiStatus"),
        ("WMAN-IF-ASDRAFT1-MIB", "wmanIfSsRssiStatusInfo"))
)
if mibBuilder.loadTexts:
    wmanSsRssiStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WMAN-IF-ASDRAFT1-MIB",
    **{"VariableMacAddress": VariableMacAddress,
       "WmanIfSfSchedulingType": WmanIfSfSchedulingType,
       "WmanIfClassifierBitMap": WmanIfClassifierBitMap,
       "WmanIfOfdmFecCodeType": WmanIfOfdmFecCodeType,
       "wmanIfMib": wmanIfMib,
       "wmanIfMibObjects": wmanIfMibObjects,
       "wmanIfBsObjects": wmanIfBsObjects,
       "wmanIfBsPacketCs": wmanIfBsPacketCs,
       "wmanIfBsProvisionedSfTable": wmanIfBsProvisionedSfTable,
       "wmanIfBsProvisionedSfEntry": wmanIfBsProvisionedSfEntry,
       "wmanIfBsSfId": wmanIfBsSfId,
       "wmanIfBsSsProvMacAddress": wmanIfBsSsProvMacAddress,
       "wmanIfBsSfDirection": wmanIfBsSfDirection,
       "wmanIfBsServiceClassIndex": wmanIfBsServiceClassIndex,
       "wmanIfBsServiceClassName": wmanIfBsServiceClassName,
       "wmanIfBsSfState": wmanIfBsSfState,
       "wmanIfBsSfProvisionedTime": wmanIfBsSfProvisionedTime,
       "wmanIfBsProvisionedSfRowStatus": wmanIfBsProvisionedSfRowStatus,
       "wmanIfBsServiceClassTable": wmanIfBsServiceClassTable,
       "wmanIfBsServiceClassEntry": wmanIfBsServiceClassEntry,
       "wmanIfBsQoSProfileIndex": wmanIfBsQoSProfileIndex,
       "wmanIfBsQosServiceClassName": wmanIfBsQosServiceClassName,
       "wmanIfBsQoSTrafficPriority": wmanIfBsQoSTrafficPriority,
       "wmanIfBsQoSMaxSustainedRate": wmanIfBsQoSMaxSustainedRate,
       "wmanIfBsQoSMaxTrafficBurst": wmanIfBsQoSMaxTrafficBurst,
       "wmanIfBsQoSMinReservedRate": wmanIfBsQoSMinReservedRate,
       "wmanIfBsQoSToleratedJitter": wmanIfBsQoSToleratedJitter,
       "wmanIfBsQoSMaxLatency": wmanIfBsQoSMaxLatency,
       "wmanIfBsQoSFixedVsVariableSduInd": wmanIfBsQoSFixedVsVariableSduInd,
       "wmanIfBsQoSSduSize": wmanIfBsQoSSduSize,
       "wmanIfBsQosScSchedulingType": wmanIfBsQosScSchedulingType,
       "wmanIfBsQosScArqEnable": wmanIfBsQosScArqEnable,
       "wmanIfBsQosScArqWindowSize": wmanIfBsQosScArqWindowSize,
       "wmanIfBsQosScArqFragmentLifetime": wmanIfBsQosScArqFragmentLifetime,
       "wmanIfBsQosScArqSyncLossTimeout": wmanIfBsQosScArqSyncLossTimeout,
       "wmanIfBsQosScArqDeliverInOrder": wmanIfBsQosScArqDeliverInOrder,
       "wmanIfBsQosScArqRxPurgeTimeout": wmanIfBsQosScArqRxPurgeTimeout,
       "wmanIfBsQosScArqBlockSize": wmanIfBsQosScArqBlockSize,
       "wmanIfBsQosSCMinRsvdTolerableRate": wmanIfBsQosSCMinRsvdTolerableRate,
       "wmanIfBsQoSReqTxPolicy": wmanIfBsQoSReqTxPolicy,
       "wmanIfBsQoSServiceClassRowStatus": wmanIfBsQoSServiceClassRowStatus,
       "wmanIfBsClassifierRuleTable": wmanIfBsClassifierRuleTable,
       "wmanIfBsClassifierRuleEntry": wmanIfBsClassifierRuleEntry,
       "wmanIfBsSfIndex": wmanIfBsSfIndex,
       "wmanIfBsClassifierRuleIndex": wmanIfBsClassifierRuleIndex,
       "wmanIfBsClassifierRulePriority": wmanIfBsClassifierRulePriority,
       "wmanIfBsClassifierRuleIpTosLow": wmanIfBsClassifierRuleIpTosLow,
       "wmanIfBsClassifierRuleIpTosHigh": wmanIfBsClassifierRuleIpTosHigh,
       "wmanIfBsClassifierRuleIpTosMask": wmanIfBsClassifierRuleIpTosMask,
       "wmanIfBsClassifierRuleIpProtocol": wmanIfBsClassifierRuleIpProtocol,
       "wmanIfBsClassifierRuleIpAddressType": wmanIfBsClassifierRuleIpAddressType,
       "wmanIfBsClassifierRuleIpSourceAddr": wmanIfBsClassifierRuleIpSourceAddr,
       "wmanIfBsClassifierRuleIpSourceMask": wmanIfBsClassifierRuleIpSourceMask,
       "wmanIfBsClassifierRuleIpDestAddr": wmanIfBsClassifierRuleIpDestAddr,
       "wmanIfBsClassifierRuleIpDestMask": wmanIfBsClassifierRuleIpDestMask,
       "wmanIfBsClassifierRuleSourcePortStart": wmanIfBsClassifierRuleSourcePortStart,
       "wmanIfBsClassifierRuleSourcePortEnd": wmanIfBsClassifierRuleSourcePortEnd,
       "wmanIfBsClassifierRuleDestPortStart": wmanIfBsClassifierRuleDestPortStart,
       "wmanIfBsClassifierRuleDestPortEnd": wmanIfBsClassifierRuleDestPortEnd,
       "wmanIfBsClassifierRuleDestMacAddr": wmanIfBsClassifierRuleDestMacAddr,
       "wmanIfBsClassifierRuleDestMacMask": wmanIfBsClassifierRuleDestMacMask,
       "wmanIfBsClassifierRuleSourceMacAddr": wmanIfBsClassifierRuleSourceMacAddr,
       "wmanIfBsClassifierRuleSourceMacMask": wmanIfBsClassifierRuleSourceMacMask,
       "wmanIfBsClassifierRuleEnetProtocolType": wmanIfBsClassifierRuleEnetProtocolType,
       "wmanIfBsClassifierRuleEnetProtocol": wmanIfBsClassifierRuleEnetProtocol,
       "wmanIfBsClassifierRuleUserPriLow": wmanIfBsClassifierRuleUserPriLow,
       "wmanIfBsClassifierRuleUserPriHigh": wmanIfBsClassifierRuleUserPriHigh,
       "wmanIfBsClassifierRuleVlanId": wmanIfBsClassifierRuleVlanId,
       "wmanIfBsClassifierRuleState": wmanIfBsClassifierRuleState,
       "wmanIfBsClassifierRulePkts": wmanIfBsClassifierRulePkts,
       "wmanIfBSClassifierRuleBitMap": wmanIfBSClassifierRuleBitMap,
       "wmanIfBsClassifierRuleRowStatus": wmanIfBsClassifierRuleRowStatus,
       "wmanIfBsSsPacketCounterTable": wmanIfBsSsPacketCounterTable,
       "wmanIfBsSsPacketCounterEntry": wmanIfBsSsPacketCounterEntry,
       "wmanIfBsSsSfIndex": wmanIfBsSsSfIndex,
       "wmanIfBsSsPktMacAddr": wmanIfBsSsPktMacAddr,
       "wmanIfBsSsSfDirection": wmanIfBsSsSfDirection,
       "wmanIfBsSsMacSduCount": wmanIfBsSsMacSduCount,
       "wmanIfBsSsOctetCount": wmanIfBsSsOctetCount,
       "wmanIfBsSsResetCounter": wmanIfBsSsResetCounter,
       "wmanIfBsSsResetCounterTime": wmanIfBsSsResetCounterTime,
       "wmanIfBsCps": wmanIfBsCps,
       "wmanIfBsRegisteredSsTable": wmanIfBsRegisteredSsTable,
       "wmanIfBsRegisteredSsEntry": wmanIfBsRegisteredSsEntry,
       "wmanIfBsSsIdIndex": wmanIfBsSsIdIndex,
       "wmanIfBsSsMacAddress": wmanIfBsSsMacAddress,
       "wmanIfBsSsBasicCid": wmanIfBsSsBasicCid,
       "wmanIfBsSsPrimaryCid": wmanIfBsSsPrimaryCid,
       "wmanIfBsSsSecondaryCid": wmanIfBsSsSecondaryCid,
       "wmanIfBsSsHmacTuple": wmanIfBsSsHmacTuple,
       "wmanIfBsSsUlCidSupport": wmanIfBsSsUlCidSupport,
       "wmanIfBsSsManagementSupport": wmanIfBsSsManagementSupport,
       "wmanIfBsSsArqSupport": wmanIfBsSsArqSupport,
       "wmanIfBsSsDsxFlowControl": wmanIfBsSsDsxFlowControl,
       "wmanIfBsSsMacCrcSupport": wmanIfBsSsMacCrcSupport,
       "wmanIfBsSsMcaFlowControl": wmanIfBsSsMcaFlowControl,
       "wmanIfBsSsMcpGroupCidSupport": wmanIfBsSsMcpGroupCidSupport,
       "wmanIfBsSsPkmFlowControl": wmanIfBsSsPkmFlowControl,
       "wmanIfBsSsAuthorizationPolicyControl": wmanIfBsSsAuthorizationPolicyControl,
       "wmanIfBsSsMaxNumOfSupportedSA": wmanIfBsSsMaxNumOfSupportedSA,
       "wmanIfBsSsIpVersion": wmanIfBsSsIpVersion,
       "wmanIfBsSsMacCsSupportBitMap": wmanIfBsSsMacCsSupportBitMap,
       "wmanIfBsSsMaxNumOfClassifier": wmanIfBsSsMaxNumOfClassifier,
       "wmanIfBsSsPhsSupport": wmanIfBsSsPhsSupport,
       "wmanIfBsSsIpManagementSupport": wmanIfBsSsIpManagementSupport,
       "wmanIfBsSs2ndMgmtArqEnable": wmanIfBsSs2ndMgmtArqEnable,
       "wmanIfBsSs2ndMgmtArqWindowSize": wmanIfBsSs2ndMgmtArqWindowSize,
       "wmanIfBsSs2ndMgmtArqFragmentLifetime": wmanIfBsSs2ndMgmtArqFragmentLifetime,
       "wmanIfBsSs2ndMgmtArqSyncLossTimeout": wmanIfBsSs2ndMgmtArqSyncLossTimeout,
       "wmanIfBsSs2ndMgmtArqDeliverInOrder": wmanIfBsSs2ndMgmtArqDeliverInOrder,
       "wmanIfBsSs2ndMgmtArqRxPurgeTimeout": wmanIfBsSs2ndMgmtArqRxPurgeTimeout,
       "wmanIfBsSsVendorIdEncoding": wmanIfBsSsVendorIdEncoding,
       "wmanIfBsConfigurationTable": wmanIfBsConfigurationTable,
       "wmanIfBsConfigurationEntry": wmanIfBsConfigurationEntry,
       "wmanIfBsDcdInterval": wmanIfBsDcdInterval,
       "wmanIfBsUcdInterval": wmanIfBsUcdInterval,
       "wmanIfBsUcdTransition": wmanIfBsUcdTransition,
       "wmanIfBsDcdTransition": wmanIfBsDcdTransition,
       "wmanIfBsMaxMAPPending": wmanIfBsMaxMAPPending,
       "wmanIfBsInitialRangingInterval": wmanIfBsInitialRangingInterval,
       "wmanIfBsClkCmpInterval": wmanIfBsClkCmpInterval,
       "wmanIfBsSsULMapProcTime": wmanIfBsSsULMapProcTime,
       "wmanIfBsSsRangRespProcTime": wmanIfBsSsRangRespProcTime,
       "wmanIfBsT5Timeout": wmanIfBsT5Timeout,
       "wmanIfBsT9Timeout": wmanIfBsT9Timeout,
       "wmanIfBsT13Timeout": wmanIfBsT13Timeout,
       "wmanIfBsT15Timeout": wmanIfBsT15Timeout,
       "wmanIfBsT17Timeout": wmanIfBsT17Timeout,
       "wmanIfBsT27IdleTimer": wmanIfBsT27IdleTimer,
       "wmanIfBsT27ActiveTimer": wmanIfBsT27ActiveTimer,
       "wmanIfBsStatisticCounter": wmanIfBsStatisticCounter,
       "wmanIfBsChMeasurementTable": wmanIfBsChMeasurementTable,
       "wmanIfBsChMeasurementEntry": wmanIfBsChMeasurementEntry,
       "wmanIfBsChSsIdIndex": wmanIfBsChSsIdIndex,
       "wmanIfBsHistogramIndex": wmanIfBsHistogramIndex,
       "wmanIfBsChannelNumber": wmanIfBsChannelNumber,
       "wmanIfBsStartFrame": wmanIfBsStartFrame,
       "wmanIfBsDuration": wmanIfBsDuration,
       "wmanIfBsBasicReport": wmanIfBsBasicReport,
       "wmanIfBsMeanCinrReport": wmanIfBsMeanCinrReport,
       "wmanIfBsMeanRssiReport": wmanIfBsMeanRssiReport,
       "wmanIfBsStdDeviationCinrReport": wmanIfBsStdDeviationCinrReport,
       "wmanIfBsStdDeviationRssiReport": wmanIfBsStdDeviationRssiReport,
       "wmanIfBsFecCounterTable": wmanIfBsFecCounterTable,
       "wmanIfBsFecCounterEntry": wmanIfBsFecCounterEntry,
       "wmanIfBsFecSsId": wmanIfBsFecSsId,
       "wmanIfBsFecCorrectedBytes": wmanIfBsFecCorrectedBytes,
       "wmanIfBsFecUncorrectedBytes": wmanIfBsFecUncorrectedBytes,
       "wmanIfBsFecUncorrectedMacPdu": wmanIfBsFecUncorrectedMacPdu,
       "wmanIfBsFecResetCounter": wmanIfBsFecResetCounter,
       "wmanIfBsPkmObjects": wmanIfBsPkmObjects,
       "wmanIfBsPkmBaseTable": wmanIfBsPkmBaseTable,
       "wmanIfBsPkmBaseEntry": wmanIfBsPkmBaseEntry,
       "wmanIfBsPkmDefaultAuthLifetime": wmanIfBsPkmDefaultAuthLifetime,
       "wmanIfBsPkmDefaultTEKLifetime": wmanIfBsPkmDefaultTEKLifetime,
       "wmanIfBsPkmDefaultSelfSigManufCertTrust": wmanIfBsPkmDefaultSelfSigManufCertTrust,
       "wmanIfBsPkmCheckCertValidityPeriods": wmanIfBsPkmCheckCertValidityPeriods,
       "wmanIfBsPkmAuthentInfos": wmanIfBsPkmAuthentInfos,
       "wmanIfBsPkmAuthRequests": wmanIfBsPkmAuthRequests,
       "wmanIfBsPkmAuthReplies": wmanIfBsPkmAuthReplies,
       "wmanIfBsPkmAuthRejects": wmanIfBsPkmAuthRejects,
       "wmanIfBsPkmAuthInvalids": wmanIfBsPkmAuthInvalids,
       "wmanIfBsPkmAuthTable": wmanIfBsPkmAuthTable,
       "wmanIfBsPkmAuthEntry": wmanIfBsPkmAuthEntry,
       "wmanIfBsPkmAuthSsMacAddress": wmanIfBsPkmAuthSsMacAddress,
       "wmanIfBsPkmAuthSsPublicKey": wmanIfBsPkmAuthSsPublicKey,
       "wmanIfBsPkmAuthSsKeySequenceNumber": wmanIfBsPkmAuthSsKeySequenceNumber,
       "wmanIfBsPkmAuthSsExpiresOld": wmanIfBsPkmAuthSsExpiresOld,
       "wmanIfBsPkmAuthSsExpiresNew": wmanIfBsPkmAuthSsExpiresNew,
       "wmanIfBsPkmAuthSsLifetime": wmanIfBsPkmAuthSsLifetime,
       "wmanIfBsPkmAuthSsReset": wmanIfBsPkmAuthSsReset,
       "wmanIfBsPkmAuthSsInfos": wmanIfBsPkmAuthSsInfos,
       "wmanIfBsPkmAuthSsRequests": wmanIfBsPkmAuthSsRequests,
       "wmanIfBsPkmAuthSsReplies": wmanIfBsPkmAuthSsReplies,
       "wmanIfBsPkmAuthSsRejects": wmanIfBsPkmAuthSsRejects,
       "wmanIfBsPkmAuthSsInvalids": wmanIfBsPkmAuthSsInvalids,
       "wmanIfBsPkmAuthRejectErrorCode": wmanIfBsPkmAuthRejectErrorCode,
       "wmanIfBsPkmAuthRejectErrorString": wmanIfBsPkmAuthRejectErrorString,
       "wmanIfBsPkmAuthInvalidErrorCode": wmanIfBsPkmAuthInvalidErrorCode,
       "wmanIfBsPkmAuthInvalidErrorString": wmanIfBsPkmAuthInvalidErrorString,
       "wmanIfBsPkmAuthPrimarySAId": wmanIfBsPkmAuthPrimarySAId,
       "wmanIfBsPkmAuthBpkmSsCertValid": wmanIfBsPkmAuthBpkmSsCertValid,
       "wmanIfBsPkmAuthBpkmSsCert": wmanIfBsPkmAuthBpkmSsCert,
       "wmanIfBsPkmTEKTable": wmanIfBsPkmTEKTable,
       "wmanIfBsPkmTEKEntry": wmanIfBsPkmTEKEntry,
       "wmanIfBsPkmTEKSAId": wmanIfBsPkmTEKSAId,
       "wmanIfBsPkmTEKSAType": wmanIfBsPkmTEKSAType,
       "wmanIfBsPkmTEKDataEncryptAlg": wmanIfBsPkmTEKDataEncryptAlg,
       "wmanIfBsPkmTEKDataAuthentAlg": wmanIfBsPkmTEKDataAuthentAlg,
       "wmanIfBsPkmTEKEncryptAlg": wmanIfBsPkmTEKEncryptAlg,
       "wmanIfBsPkmTEKLifetime": wmanIfBsPkmTEKLifetime,
       "wmanIfBsPkmTEKKeySequenceNumber": wmanIfBsPkmTEKKeySequenceNumber,
       "wmanIfBsPkmTEKExpiresOld": wmanIfBsPkmTEKExpiresOld,
       "wmanIfBsPkmTEKExpiresNew": wmanIfBsPkmTEKExpiresNew,
       "wmanIfBsPkmTEKReset": wmanIfBsPkmTEKReset,
       "wmanIfBsPkmKeyRequests": wmanIfBsPkmKeyRequests,
       "wmanIfBsPkmKeyReplies": wmanIfBsPkmKeyReplies,
       "wmanIfBsPkmKeyRejects": wmanIfBsPkmKeyRejects,
       "wmanIfBsPkmTEKInvalids": wmanIfBsPkmTEKInvalids,
       "wmanIfBsPkmKeyRejectErrorCode": wmanIfBsPkmKeyRejectErrorCode,
       "wmanIfBsPkmKeyRejectErrorString": wmanIfBsPkmKeyRejectErrorString,
       "wmanIfBsPkmTEKInvalidErrorCode": wmanIfBsPkmTEKInvalidErrorCode,
       "wmanIfBsPkmTEKInvalidErrorString": wmanIfBsPkmTEKInvalidErrorString,
       "wmanIfBsNotification": wmanIfBsNotification,
       "wmanIfBsTrapDefinitions": wmanIfBsTrapDefinitions,
       "wmanIfBsThresholdConfigTable": wmanIfBsThresholdConfigTable,
       "wmanIfBsThresholdConfigEntry": wmanIfBsThresholdConfigEntry,
       "wmanIfBsRssiLowThreshold": wmanIfBsRssiLowThreshold,
       "wmanIfBsRssiHighThreshold": wmanIfBsRssiHighThreshold,
       "wmanIfBsTempLowAlarmThreshold": wmanIfBsTempLowAlarmThreshold,
       "wmanIfBsTempLowAlarmRestoredThreshold": wmanIfBsTempLowAlarmRestoredThreshold,
       "wmanIfBsTempHighAlarmThreshold": wmanIfBsTempHighAlarmThreshold,
       "wmanIfBsTempHighAlarmRestoredThreshold": wmanIfBsTempHighAlarmRestoredThreshold,
       "wmanIfBsSsNotificationObjectsTable": wmanIfBsSsNotificationObjectsTable,
       "wmanIfBsSsNotificationObjectsEntry": wmanIfBsSsNotificationObjectsEntry,
       "wmanIfBsTrapSsId": wmanIfBsTrapSsId,
       "wmanIfBsSsNotMacAddr": wmanIfBsSsNotMacAddr,
       "wmanIfBsSsStatusValue": wmanIfBsSsStatusValue,
       "wmanIfBsSsStatusInfo": wmanIfBsSsStatusInfo,
       "wmanIfBsDynamicServiceType": wmanIfBsDynamicServiceType,
       "wmanIfBsDynamicServiceFailReason": wmanIfBsDynamicServiceFailReason,
       "wmanIfBsSsRssiStatus": wmanIfBsSsRssiStatus,
       "wmanIfBsSsRssiStatusInfo": wmanIfBsSsRssiStatusInfo,
       "wmanBsSsStatusNotificationTrap": wmanBsSsStatusNotificationTrap,
       "wmanBsSsDynamicServiceFailTrap": wmanBsSsDynamicServiceFailTrap,
       "wmanBsSsRssiStatusChangeTrap": wmanBsSsRssiStatusChangeTrap,
       "wmanBsSsBPKMFailTrap": wmanBsSsBPKMFailTrap,
       "wmanIfBsNotificationObjectsTable": wmanIfBsNotificationObjectsTable,
       "wmanIfBsNotificationObjectsEntry": wmanIfBsNotificationObjectsEntry,
       "wmanIfBsPowerStatus": wmanIfBsPowerStatus,
       "wmanIfBsFanStatus": wmanIfBsFanStatus,
       "wmanIfBsTemperatureStatus": wmanIfBsTemperatureStatus,
       "wmanIfBsPowerStatusInfo": wmanIfBsPowerStatusInfo,
       "wmanIfBsFanStatusInfo": wmanIfBsFanStatusInfo,
       "wmanIfBsTemperatureStatusInfo": wmanIfBsTemperatureStatusInfo,
       "wmanBsPowerStatusChangeTrap": wmanBsPowerStatusChangeTrap,
       "wmanBsFanStatusTrap": wmanBsFanStatusTrap,
       "wmanBsTemperatureChangeTrap": wmanBsTemperatureChangeTrap,
       "wmanIfBsTrapControl": wmanIfBsTrapControl,
       "wmanIfBsTrapControlRegister": wmanIfBsTrapControlRegister,
       "wmanIfSsObjects": wmanIfSsObjects,
       "wmanIfSsCps": wmanIfSsCps,
       "wmanIfSsConfigFileEncodingTable": wmanIfSsConfigFileEncodingTable,
       "wmanIfSsConfigFileEncodingEntry": wmanIfSsConfigFileEncodingEntry,
       "wmanIfSsMicConfigSetting": wmanIfSsMicConfigSetting,
       "wmanIfSsVendorId": wmanIfSsVendorId,
       "wmanIfSsHwId": wmanIfSsHwId,
       "wmanIfSsSwVersion": wmanIfSsSwVersion,
       "wmanIfSsUpgradeFileName": wmanIfSsUpgradeFileName,
       "wmanIfSsSwUpgradeTftpServer": wmanIfSsSwUpgradeTftpServer,
       "wmanIfSsTftpServerTimeStamp": wmanIfSsTftpServerTimeStamp,
       "wmanIfSsConfigurationTable": wmanIfSsConfigurationTable,
       "wmanIfSsConfigurationEntry": wmanIfSsConfigurationEntry,
       "wmanIfSsLostDLMapInterval": wmanIfSsLostDLMapInterval,
       "wmanIfSsLostULMapInterval": wmanIfSsLostULMapInterval,
       "wmanIfSsContentionRangRetries": wmanIfSsContentionRangRetries,
       "wmanIfSsRequestRetries": wmanIfSsRequestRetries,
       "wmanIfSsRegRequestRetries": wmanIfSsRegRequestRetries,
       "wmanIfSsTftpBackoffStart": wmanIfSsTftpBackoffStart,
       "wmanIfSsTftpBackoffEnd": wmanIfSsTftpBackoffEnd,
       "wmanIfSsTftpRequestRetries": wmanIfSsTftpRequestRetries,
       "wmanIfSsTftpDownloadRetries": wmanIfSsTftpDownloadRetries,
       "wmanIfSsTftpWait": wmanIfSsTftpWait,
       "wmanIfSsToDRetries": wmanIfSsToDRetries,
       "wmanIfSsToDRetryPeriod": wmanIfSsToDRetryPeriod,
       "wmanIfSsT1Timeout": wmanIfSsT1Timeout,
       "wmanIfSsT2Timeout": wmanIfSsT2Timeout,
       "wmanIfSsT3Timeout": wmanIfSsT3Timeout,
       "wmanIfSsT4Timeout": wmanIfSsT4Timeout,
       "wmanIfSsT6Timeout": wmanIfSsT6Timeout,
       "wmanIfSsT12Timeout": wmanIfSsT12Timeout,
       "wmanIfSsT14Timeout": wmanIfSsT14Timeout,
       "wmanIfSsT16Timeout": wmanIfSsT16Timeout,
       "wmanIfSsT18Timeout": wmanIfSsT18Timeout,
       "wmanIfSsT19Timeout": wmanIfSsT19Timeout,
       "wmanIfSsT20Timeout": wmanIfSsT20Timeout,
       "wmanIfSsT21Timeout": wmanIfSsT21Timeout,
       "wmanIfSsSBCRequestRetries": wmanIfSsSBCRequestRetries,
       "wmanIfSsTftpCpltRetries": wmanIfSsTftpCpltRetries,
       "wmanIfSsT26Timeout": wmanIfSsT26Timeout,
       "wmanIfSsDLManagProcTime": wmanIfSsDLManagProcTime,
       "wmanIfSsPkmObjects": wmanIfSsPkmObjects,
       "wmanIfSsPkmBaseTable": wmanIfSsPkmBaseTable,
       "wmanIfSsPkmBaseEntry": wmanIfSsPkmBaseEntry,
       "wmanIfSsPkmPrivacyEnable": wmanIfSsPkmPrivacyEnable,
       "wmanIfSsPkmPublicKey": wmanIfSsPkmPublicKey,
       "wmanIfSsPkmAuthGraceTime": wmanIfSsPkmAuthGraceTime,
       "wmanIfSsPkmTEKGraceTime": wmanIfSsPkmTEKGraceTime,
       "wmanIfSsPkmAuthWaitTimeout": wmanIfSsPkmAuthWaitTimeout,
       "wmanIfSsPkmReauthWaitTimeout": wmanIfSsPkmReauthWaitTimeout,
       "wmanIfSsPkmOpWaitTimeout": wmanIfSsPkmOpWaitTimeout,
       "wmanIfSsPkmRekeyWaitTimeout": wmanIfSsPkmRekeyWaitTimeout,
       "wmanIfSsPkmAuthRejectWaitTimeout": wmanIfSsPkmAuthRejectWaitTimeout,
       "wmanIfSsPkmAuthTable": wmanIfSsPkmAuthTable,
       "wmanIfSsPkmAuthEntry": wmanIfSsPkmAuthEntry,
       "wmanIfSsPkmAuthState": wmanIfSsPkmAuthState,
       "wmanIfSsPkmAuthKeySequenceNumber": wmanIfSsPkmAuthKeySequenceNumber,
       "wmanIfSsPkmAuthExpiresOld": wmanIfSsPkmAuthExpiresOld,
       "wmanIfSsPkmAuthExpiresNew": wmanIfSsPkmAuthExpiresNew,
       "wmanIfSsPkmAuthReset": wmanIfSsPkmAuthReset,
       "wmanIfSsPkmAuthentInfos": wmanIfSsPkmAuthentInfos,
       "wmanIfSsPkmAuthRequests": wmanIfSsPkmAuthRequests,
       "wmanIfSsPkmAuthReplies": wmanIfSsPkmAuthReplies,
       "wmanIfSsPkmAuthRejects": wmanIfSsPkmAuthRejects,
       "wmanIfSsPkmAuthInvalids": wmanIfSsPkmAuthInvalids,
       "wmanIfSsPkmAuthRejectErrorCode": wmanIfSsPkmAuthRejectErrorCode,
       "wmanIfSsPkmAuthRejectErrorString": wmanIfSsPkmAuthRejectErrorString,
       "wmanIfSsPkmAuthInvalidErrorCode": wmanIfSsPkmAuthInvalidErrorCode,
       "wmanIfSsPkmAuthInvalidErrorString": wmanIfSsPkmAuthInvalidErrorString,
       "wmanIfSsPkmTEKTable": wmanIfSsPkmTEKTable,
       "wmanIfSsPkmTEKEntry": wmanIfSsPkmTEKEntry,
       "wmanIfSsPkmTEKSAId": wmanIfSsPkmTEKSAId,
       "wmanIfSsPkmTEKSAType": wmanIfSsPkmTEKSAType,
       "wmanIfSsPkmTEKDataEncryptAlg": wmanIfSsPkmTEKDataEncryptAlg,
       "wmanIfSsPkmTEKDataAuthentAlg": wmanIfSsPkmTEKDataAuthentAlg,
       "wmanIfSsPkmTEKEncryptAlg": wmanIfSsPkmTEKEncryptAlg,
       "wmanIfSsPkmTEKState": wmanIfSsPkmTEKState,
       "wmanIfSsPkmTEKKeySequenceNumber": wmanIfSsPkmTEKKeySequenceNumber,
       "wmanIfSsPkmTEKExpiresOld": wmanIfSsPkmTEKExpiresOld,
       "wmanIfSsPkmTEKExpiresNew": wmanIfSsPkmTEKExpiresNew,
       "wmanIfSsPkmTEKKeyRequests": wmanIfSsPkmTEKKeyRequests,
       "wmanIfSsPkmTEKKeyReplies": wmanIfSsPkmTEKKeyReplies,
       "wmanIfSsPkmTEKKeyRejects": wmanIfSsPkmTEKKeyRejects,
       "wmanIfSsPkmTEKInvalids": wmanIfSsPkmTEKInvalids,
       "wmanIfSsPkmTEKAuthPends": wmanIfSsPkmTEKAuthPends,
       "wmanIfSsPkmTEKKeyRejectErrorCode": wmanIfSsPkmTEKKeyRejectErrorCode,
       "wmanIfSsPkmTEKKeyRejectErrorString": wmanIfSsPkmTEKKeyRejectErrorString,
       "wmanIfSsPkmTEKInvalidErrorCode": wmanIfSsPkmTEKInvalidErrorCode,
       "wmanIfSsPkmTEKInvalidErrorString": wmanIfSsPkmTEKInvalidErrorString,
       "wmanIfSsDeviceCertTable": wmanIfSsDeviceCertTable,
       "wmanIfSsDeviceCertEntry": wmanIfSsDeviceCertEntry,
       "wmanIfSsDeviceCert": wmanIfSsDeviceCert,
       "wmanIfSsDeviceManufCert": wmanIfSsDeviceManufCert,
       "wmanIfSsNotification": wmanIfSsNotification,
       "wmanIfSsTrapDefinitions": wmanIfSsTrapDefinitions,
       "wmanSsTLVUnknownTrap": wmanSsTLVUnknownTrap,
       "wmanSsDynamicServiceFailTrap": wmanSsDynamicServiceFailTrap,
       "wmanSsDHCPSuccessTrap": wmanSsDHCPSuccessTrap,
       "wmanSsRssiStatusChangeTrap": wmanSsRssiStatusChangeTrap,
       "wmanIfSsNotificationObjectsTable": wmanIfSsNotificationObjectsTable,
       "wmanIfSsNotificationObjectsEntry": wmanIfSsNotificationObjectsEntry,
       "wmanIfSsMacAddress": wmanIfSsMacAddress,
       "wmanIfSsUnknownTlv": wmanIfSsUnknownTlv,
       "wmanIfSsDynamicServiceType": wmanIfSsDynamicServiceType,
       "wmanIfSsDynamicServiceFailReason": wmanIfSsDynamicServiceFailReason,
       "wmanIfSsRssiStatus": wmanIfSsRssiStatus,
       "wmanIfSsRssiStatusInfo": wmanIfSsRssiStatusInfo,
       "wmanIfSsTrapControl": wmanIfSsTrapControl,
       "wmanIfSsTrapControlRegister": wmanIfSsTrapControlRegister,
       "wmanIfSsThresholdConfigTable": wmanIfSsThresholdConfigTable,
       "wmanIfSsThresholdConfigEntry": wmanIfSsThresholdConfigEntry,
       "wmanIfSsRssiLowThreshold": wmanIfSsRssiLowThreshold,
       "wmanIfSsRssiHighThreshold": wmanIfSsRssiHighThreshold,
       "wmanIfCommonObjects": wmanIfCommonObjects,
       "wmanIfCmnPacketCs": wmanIfCmnPacketCs,
       "wmanIfCmnClassifierRuleTable": wmanIfCmnClassifierRuleTable,
       "wmanIfCmnClassifierRuleEntry": wmanIfCmnClassifierRuleEntry,
       "wmanIfCmnClassifierRuleIndex": wmanIfCmnClassifierRuleIndex,
       "wmanIfCmnCpsSfIndex": wmanIfCmnCpsSfIndex,
       "wmanIfCmnClassifierRulePriority": wmanIfCmnClassifierRulePriority,
       "wmanIfCmnClassifierRuleIpTosLow": wmanIfCmnClassifierRuleIpTosLow,
       "wmanIfCmnClassifierRuleIpTosHigh": wmanIfCmnClassifierRuleIpTosHigh,
       "wmanIfCmnClassifierRuleIpTosMask": wmanIfCmnClassifierRuleIpTosMask,
       "wmanIfCmnClassifierRuleIpProtocol": wmanIfCmnClassifierRuleIpProtocol,
       "wmanIfCmnClassifierRuleIpAddressType": wmanIfCmnClassifierRuleIpAddressType,
       "wmanIfCmnClassifierRuleIpSourceAddr": wmanIfCmnClassifierRuleIpSourceAddr,
       "wmanIfCmnClassifierRuleIpSourceMask": wmanIfCmnClassifierRuleIpSourceMask,
       "wmanIfCmnClassifierRuleIpDestAddr": wmanIfCmnClassifierRuleIpDestAddr,
       "wmanIfCmnClassifierRuleIpDestMask": wmanIfCmnClassifierRuleIpDestMask,
       "wmanIfCmnClassifierRuleSourcePortStart": wmanIfCmnClassifierRuleSourcePortStart,
       "wmanIfCmnClassifierRuleSourcePortEnd": wmanIfCmnClassifierRuleSourcePortEnd,
       "wmanIfCmnClassifierRuleDestPortStart": wmanIfCmnClassifierRuleDestPortStart,
       "wmanIfCmnClassifierRuleDestPortEnd": wmanIfCmnClassifierRuleDestPortEnd,
       "wmanIfCmnClassifierRuleDestMacAddr": wmanIfCmnClassifierRuleDestMacAddr,
       "wmanIfCmnClassifierRuleDestMacMask": wmanIfCmnClassifierRuleDestMacMask,
       "wmanIfCmnClassifierRuleSourceMacAddr": wmanIfCmnClassifierRuleSourceMacAddr,
       "wmanIfCmnClassifierRuleSourceMacMask": wmanIfCmnClassifierRuleSourceMacMask,
       "wmanIfCmnClassifierRuleEnetProtocolType": wmanIfCmnClassifierRuleEnetProtocolType,
       "wmanIfCmnClassifierRuleEnetProtocol": wmanIfCmnClassifierRuleEnetProtocol,
       "wmanIfCmnClassifierRuleUserPriLow": wmanIfCmnClassifierRuleUserPriLow,
       "wmanIfCmnClassifierRuleUserPriHigh": wmanIfCmnClassifierRuleUserPriHigh,
       "wmanIfCmnClassifierRuleVlanId": wmanIfCmnClassifierRuleVlanId,
       "wmanIfCmnClassifierRuleState": wmanIfCmnClassifierRuleState,
       "wmanIfCmnClassifierRulePkts": wmanIfCmnClassifierRulePkts,
       "wmanIfCmnClassifierRuleBitMap": wmanIfCmnClassifierRuleBitMap,
       "wmanIfCmnCps": wmanIfCmnCps,
       "wmanIfCmnCpsServiceFlowTable": wmanIfCmnCpsServiceFlowTable,
       "wmanIfCmnCpsServiceFlowEntry": wmanIfCmnCpsServiceFlowEntry,
       "wmanIfCmnCpsSfId": wmanIfCmnCpsSfId,
       "wmanIfCmnCpsSfCid": wmanIfCmnCpsSfCid,
       "wmanIfCmnCpsSfDirection": wmanIfCmnCpsSfDirection,
       "wmanIfCmnCpsSfState": wmanIfCmnCpsSfState,
       "wmanIfCmnCpsServiceClassName": wmanIfCmnCpsServiceClassName,
       "wmanIfCmnCpsTrafficPriority": wmanIfCmnCpsTrafficPriority,
       "wmanIfCmnCpsMaxSustainedRate": wmanIfCmnCpsMaxSustainedRate,
       "wmanIfCmnCpsMaxTrafficBurst": wmanIfCmnCpsMaxTrafficBurst,
       "wmanIfCmnCpsMinReservedRate": wmanIfCmnCpsMinReservedRate,
       "wmanIfCmnCpsToleratedJitter": wmanIfCmnCpsToleratedJitter,
       "wmanIfCmnCpsMaxLatency": wmanIfCmnCpsMaxLatency,
       "wmanIfCmnCpsFixedVsVariableSduInd": wmanIfCmnCpsFixedVsVariableSduInd,
       "wmanIfCmnCpsSduSize": wmanIfCmnCpsSduSize,
       "wmanIfCmnCpsSfSchedulingType": wmanIfCmnCpsSfSchedulingType,
       "wmanIfCmnCpsArqEnable": wmanIfCmnCpsArqEnable,
       "wmanIfCmnCpsArqWindowSize": wmanIfCmnCpsArqWindowSize,
       "wmanIfCmnCpsArqFragmentLifetime": wmanIfCmnCpsArqFragmentLifetime,
       "wmanIfCmnCpsArqSyncLossTimeout": wmanIfCmnCpsArqSyncLossTimeout,
       "wmanIfCmnCpsArqDeliverInOrder": wmanIfCmnCpsArqDeliverInOrder,
       "wmanIfCmnCpsArqRxPurgeTimeout": wmanIfCmnCpsArqRxPurgeTimeout,
       "wmanIfCmnCpsArqBlockSize": wmanIfCmnCpsArqBlockSize,
       "wmanIfCmnCpsMinRsvdTolerableRate": wmanIfCmnCpsMinRsvdTolerableRate,
       "wmanIfCmnCpsReqTxPolicy": wmanIfCmnCpsReqTxPolicy,
       "wmanIfCmnBsSsConfigurationTable": wmanIfCmnBsSsConfigurationTable,
       "wmanIfCmnBsSsConfigurationEntry": wmanIfCmnBsSsConfigurationEntry,
       "wmanIfCmnInvitedRangRetries": wmanIfCmnInvitedRangRetries,
       "wmanIfCmnMinislotSize": wmanIfCmnMinislotSize,
       "wmanIfCmnDSxReqRetries": wmanIfCmnDSxReqRetries,
       "wmanIfCmnDSxRespRetries": wmanIfCmnDSxRespRetries,
       "wmanIfCmnT7Timeout": wmanIfCmnT7Timeout,
       "wmanIfCmnT8Timeout": wmanIfCmnT8Timeout,
       "wmanIfCmnT10Timeout": wmanIfCmnT10Timeout,
       "wmanIfCmnT22Timeout": wmanIfCmnT22Timeout,
       "wmanIfCmnSsStatCounter": wmanIfCmnSsStatCounter,
       "wmanIfCmnSsChMeasurementTable": wmanIfCmnSsChMeasurementTable,
       "wmanIfCmnSsChMeasurementEntry": wmanIfCmnSsChMeasurementEntry,
       "wmanIfCmnSsIdIndex": wmanIfCmnSsIdIndex,
       "wmanIfCmnHistogramIndex": wmanIfCmnHistogramIndex,
       "wmanIfCmnChannelNumber": wmanIfCmnChannelNumber,
       "wmanIfCmnStartFrame": wmanIfCmnStartFrame,
       "wmanIfCmnDuration": wmanIfCmnDuration,
       "wmanIfCmnBasicReport": wmanIfCmnBasicReport,
       "wmanIfCmnMeanCinrReport": wmanIfCmnMeanCinrReport,
       "wmanIfCmnStdDeviationCinrReport": wmanIfCmnStdDeviationCinrReport,
       "wmanIfCmnMeanRssiReport": wmanIfCmnMeanRssiReport,
       "wmanIfCmnStdDeviationRssiReport": wmanIfCmnStdDeviationRssiReport,
       "wmanIfCmnSsFecCounterTable": wmanIfCmnSsFecCounterTable,
       "wmanIfCmnSsFecCounterEntry": wmanIfCmnSsFecCounterEntry,
       "wmanIfCmnSsFecSsId": wmanIfCmnSsFecSsId,
       "wmanIfCmnSsFecCorrectedBytes": wmanIfCmnSsFecCorrectedBytes,
       "wmanIfCmnSsFecUncorrectedBytes": wmanIfCmnSsFecUncorrectedBytes,
       "wmanIfCmnSsFecUncorrectedMacPdu": wmanIfCmnSsFecUncorrectedMacPdu,
       "wmanIfCmnSsFecResetCounter": wmanIfCmnSsFecResetCounter,
       "wmanIfCmnPkmObjects": wmanIfCmnPkmObjects,
       "wmanIfCmnCryptoSuiteTable": wmanIfCmnCryptoSuiteTable,
       "wmanIfCmnCryptoSuiteEntry": wmanIfCmnCryptoSuiteEntry,
       "wmanIfCmnCryptoSuiteIndex": wmanIfCmnCryptoSuiteIndex,
       "wmanIfCmnCryptoSuiteDataEncryptAlg": wmanIfCmnCryptoSuiteDataEncryptAlg,
       "wmanIfCmnCryptoSuiteDataAuthentAlg": wmanIfCmnCryptoSuiteDataAuthentAlg,
       "wmanIfCmnCryptoSuiteTEKEncryptAlg": wmanIfCmnCryptoSuiteTEKEncryptAlg,
       "wmanIfCmnOfdmPhy": wmanIfCmnOfdmPhy,
       "wmanIfCmnOfdmUplinkChannelTable": wmanIfCmnOfdmUplinkChannelTable,
       "wmanIfCmnOfdmUplinkChannelEntry": wmanIfCmnOfdmUplinkChannelEntry,
       "wmanIfCmnOfdmCtBasedResvTimeout": wmanIfCmnOfdmCtBasedResvTimeout,
       "wmanIfCmnOfdmBwReqOppSize": wmanIfCmnOfdmBwReqOppSize,
       "wmanIfCmnOfdmRangReqOppSize": wmanIfCmnOfdmRangReqOppSize,
       "wmanIfCmnOfdmUplinkCenterFreq": wmanIfCmnOfdmUplinkCenterFreq,
       "wmanIfCmnOfdmSubChReqRegionFull": wmanIfCmnOfdmSubChReqRegionFull,
       "wmanIfCmnOfdmSubChFocusCtCode": wmanIfCmnOfdmSubChFocusCtCode,
       "wmanIfCmnOfdmDownlinkChannelTable": wmanIfCmnOfdmDownlinkChannelTable,
       "wmanIfCmnOfdmDownlinkChannelEntry": wmanIfCmnOfdmDownlinkChannelEntry,
       "wmanIfCmnOfdmBsEIRP": wmanIfCmnOfdmBsEIRP,
       "wmanIfCmnOfdmChannelNumber": wmanIfCmnOfdmChannelNumber,
       "wmanIfCmnOfdmTTG": wmanIfCmnOfdmTTG,
       "wmanIfCmnOfdmRTG": wmanIfCmnOfdmRTG,
       "wmanIfCmnOfdmInitRngMaxRSS": wmanIfCmnOfdmInitRngMaxRSS,
       "wmanIfCmnOfdmChSwitchFrameNmr": wmanIfCmnOfdmChSwitchFrameNmr,
       "wmanIfCmnOfdmDownlinkCenterFreq": wmanIfCmnOfdmDownlinkCenterFreq,
       "wmanIfCmnOfdmBsId": wmanIfCmnOfdmBsId,
       "wmanIfCmnOfdmMacVersion": wmanIfCmnOfdmMacVersion,
       "wmanIfCmnOfdmFrameDurationCode": wmanIfCmnOfdmFrameDurationCode,
       "wmanIfCmnOfdmFrameNumber": wmanIfCmnOfdmFrameNumber,
       "wmanIfCmnOfdmUcdBurstProfileTable": wmanIfCmnOfdmUcdBurstProfileTable,
       "wmanIfCmnOfdmUcdBurstProfileEntry": wmanIfCmnOfdmUcdBurstProfileEntry,
       "wmanIfCmnOfdmUiucIndex": wmanIfCmnOfdmUiucIndex,
       "wmanIfCmnOfdmUplinkFrequency": wmanIfCmnOfdmUplinkFrequency,
       "wmanIfCmnOfdmUcdFecCodeType": wmanIfCmnOfdmUcdFecCodeType,
       "wmanIfCmnOfdmFocusCtPowerBoost": wmanIfCmnOfdmFocusCtPowerBoost,
       "wmanIfCmnOfdmUcdBurstProfileRowStatus": wmanIfCmnOfdmUcdBurstProfileRowStatus,
       "wmanIfCmnOfdmDcdBurstProfileTable": wmanIfCmnOfdmDcdBurstProfileTable,
       "wmanIfCmnOfdmDcdBurstProfileEntry": wmanIfCmnOfdmDcdBurstProfileEntry,
       "wmanIfCmnOfdmDiucIndex": wmanIfCmnOfdmDiucIndex,
       "wmanIfCmnOfdmDownlinkFrequency": wmanIfCmnOfdmDownlinkFrequency,
       "wmanIfCmnOfdmDcdFecCodeType": wmanIfCmnOfdmDcdFecCodeType,
       "wmanIfCmnOfdmDiucMandatoryExitThresh": wmanIfCmnOfdmDiucMandatoryExitThresh,
       "wmanIfCmnOfdmDiucMinEntryThresh": wmanIfCmnOfdmDiucMinEntryThresh,
       "wmanIfCmnOfdmTcsEnable": wmanIfCmnOfdmTcsEnable,
       "wmanIfCmnOfdmDcdBurstProfileRowStatus": wmanIfCmnOfdmDcdBurstProfileRowStatus}
)
