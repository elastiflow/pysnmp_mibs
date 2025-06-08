# SNMP MIB module (CISCOSB-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-LLDP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:46 2025
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

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "CISCOSB-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rndNotifications,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rndNotifications",
    "switch001")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(LldpXMedCapabilities,) = mibBuilder.importSymbols(
    "LLDP-EXT-MED-MIB",
    "LldpXMedCapabilities")

(LldpManAddress,
 LldpPortList,
 LldpPortNumber,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpManAddress",
    "LldpPortList",
    "LldpPortNumber",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

(lldpV2LocPortIfIndex,
 lldpV2RemLocalIfIndex) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2RemLocalIfIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110)
)
if mibBuilder.loadTexts:
    rlLldp.setRevisions(
        ("2005-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )



class PolicyContainerAppType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("guestVoiceSignaling", 4),
          ("softPhoneVoice", 5),
          ("videoconferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )



class PolicyAppVoiceUpdateMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlLldpObjects_ObjectIdentity = ObjectIdentity
rlLldpObjects = _RlLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1)
)
_RlLldpConfig_ObjectIdentity = ObjectIdentity
rlLldpConfig = _RlLldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1)
)
_RlLldpEnabled_Type = TruthValue
_RlLldpEnabled_Object = MibScalar
rlLldpEnabled = _RlLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 1),
    _RlLldpEnabled_Type()
)
rlLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpEnabled.setStatus("current")


class _RlLldpClearRx_Type(PortList):
    """Custom type rlLldpClearRx based on PortList"""
    defaultHexValue = ""


_RlLldpClearRx_Type.__name__ = "PortList"
_RlLldpClearRx_Object = MibScalar
rlLldpClearRx = _RlLldpClearRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 2),
    _RlLldpClearRx_Type()
)
rlLldpClearRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpClearRx.setStatus("current")


class _RlLldpDuMode_Type(Integer32):
    """Custom type rlLldpDuMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("flooding", 2))
    )


_RlLldpDuMode_Type.__name__ = "Integer32"
_RlLldpDuMode_Object = MibScalar
rlLldpDuMode = _RlLldpDuMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 3),
    _RlLldpDuMode_Type()
)
rlLldpDuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpDuMode.setStatus("current")
_RlLldpAutoAdvLocPortManAddrTable_Object = MibTable
rlLldpAutoAdvLocPortManAddrTable = _RlLldpAutoAdvLocPortManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortManAddrTable.setStatus("current")
_RlLldpAutoAdvLocPortManAddrEntry_Object = MibTableRow
rlLldpAutoAdvLocPortManAddrEntry = _RlLldpAutoAdvLocPortManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1)
)
rlLldpAutoAdvLocPortManAddrEntry.setIndexNames(
    (0, "CISCOSB-LLDP-MIB", "rlLldpAutoAdvLocPortNum"),
)
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortManAddrEntry.setStatus("current")
_RlLldpAutoAdvLocPortNum_Type = LldpPortNumber
_RlLldpAutoAdvLocPortNum_Object = MibTableColumn
rlLldpAutoAdvLocPortNum = _RlLldpAutoAdvLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 1),
    _RlLldpAutoAdvLocPortNum_Type()
)
rlLldpAutoAdvLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortNum.setStatus("current")


class _RlLldpAutoAdvManAddrOwnerIfId_Type(Integer32):
    """Custom type rlLldpAutoAdvManAddrOwnerIfId based on Integer32"""
    defaultValue = 0


_RlLldpAutoAdvManAddrOwnerIfId_Type.__name__ = "Integer32"
_RlLldpAutoAdvManAddrOwnerIfId_Object = MibTableColumn
rlLldpAutoAdvManAddrOwnerIfId = _RlLldpAutoAdvManAddrOwnerIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 2),
    _RlLldpAutoAdvManAddrOwnerIfId_Type()
)
rlLldpAutoAdvManAddrOwnerIfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrOwnerIfId.setStatus("current")


class _RlLldpAutoAdvManAddrNone_Type(TruthValue):
    """Custom type rlLldpAutoAdvManAddrNone based on TruthValue"""
    defaultValue = 2


_RlLldpAutoAdvManAddrNone_Type.__name__ = "TruthValue"
_RlLldpAutoAdvManAddrNone_Object = MibTableColumn
rlLldpAutoAdvManAddrNone = _RlLldpAutoAdvManAddrNone_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 3),
    _RlLldpAutoAdvManAddrNone_Type()
)
rlLldpAutoAdvManAddrNone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrNone.setStatus("current")
_RlLldpAutoAdvManAddrSubtype_Type = AddressFamilyNumbers
_RlLldpAutoAdvManAddrSubtype_Object = MibTableColumn
rlLldpAutoAdvManAddrSubtype = _RlLldpAutoAdvManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 4),
    _RlLldpAutoAdvManAddrSubtype_Type()
)
rlLldpAutoAdvManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrSubtype.setStatus("current")
_RlLldpAutoAdvManAddr_Type = LldpManAddress
_RlLldpAutoAdvManAddr_Object = MibTableColumn
rlLldpAutoAdvManAddr = _RlLldpAutoAdvManAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 5),
    _RlLldpAutoAdvManAddr_Type()
)
rlLldpAutoAdvManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddr.setStatus("current")
_RlLldpAutoAdvPortsStatus_Type = RowStatus
_RlLldpAutoAdvPortsStatus_Object = MibTableColumn
rlLldpAutoAdvPortsStatus = _RlLldpAutoAdvPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 4, 1, 6),
    _RlLldpAutoAdvPortsStatus_Type()
)
rlLldpAutoAdvPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvPortsStatus.setStatus("current")


class _RlLldpChassisIdSubtype_Type(Integer32):
    """Custom type rlLldpChassisIdSubtype based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 4),
          ("local", 7))
    )


_RlLldpChassisIdSubtype_Type.__name__ = "Integer32"
_RlLldpChassisIdSubtype_Object = MibScalar
rlLldpChassisIdSubtype = _RlLldpChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 5),
    _RlLldpChassisIdSubtype_Type()
)
rlLldpChassisIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpChassisIdSubtype.setStatus("current")
_RlLldpPortConfigTable_Object = MibTable
rlLldpPortConfigTable = _RlLldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rlLldpPortConfigTable.setStatus("current")
_RlLldpPortConfigEntry_Object = MibTableRow
rlLldpPortConfigEntry = _RlLldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rlLldpPortConfigEntry.setStatus("current")


class _RlLldpPortConfig4wireTxEnable_Type(TruthValue):
    """Custom type rlLldpPortConfig4wireTxEnable based on TruthValue"""
    defaultValue = 2


_RlLldpPortConfig4wireTxEnable_Type.__name__ = "TruthValue"
_RlLldpPortConfig4wireTxEnable_Object = MibTableColumn
rlLldpPortConfig4wireTxEnable = _RlLldpPortConfig4wireTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 1, 6, 1, 1),
    _RlLldpPortConfig4wireTxEnable_Type()
)
rlLldpPortConfig4wireTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpPortConfig4wireTxEnable.setStatus("current")
_RlLldpXMedConfig_ObjectIdentity = ObjectIdentity
rlLldpXMedConfig = _RlLldpXMedConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2)
)
_RlLldpXMedLocMediaPolicyContainerTable_Object = MibTable
rlLldpXMedLocMediaPolicyContainerTable = _RlLldpXMedLocMediaPolicyContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerTable.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerEntry_Object = MibTableRow
rlLldpXMedLocMediaPolicyContainerEntry = _RlLldpXMedLocMediaPolicyContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1)
)
rlLldpXMedLocMediaPolicyContainerEntry.setIndexNames(
    (0, "CISCOSB-LLDP-MIB", "rlLldpXMedLocMediaPolicyContainerIndex"),
)
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerEntry.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerIndex_Type = PolicyNumber
_RlLldpXMedLocMediaPolicyContainerIndex_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerIndex = _RlLldpXMedLocMediaPolicyContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 1),
    _RlLldpXMedLocMediaPolicyContainerIndex_Type()
)
rlLldpXMedLocMediaPolicyContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerIndex.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerAppType_Type = PolicyContainerAppType
_RlLldpXMedLocMediaPolicyContainerAppType_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerAppType = _RlLldpXMedLocMediaPolicyContainerAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 2),
    _RlLldpXMedLocMediaPolicyContainerAppType_Type()
)
rlLldpXMedLocMediaPolicyContainerAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerAppType.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerVlanID_Type(Integer32):
    """Custom type rlLldpXMedLocMediaPolicyContainerVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_RlLldpXMedLocMediaPolicyContainerVlanID_Type.__name__ = "Integer32"
_RlLldpXMedLocMediaPolicyContainerVlanID_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerVlanID = _RlLldpXMedLocMediaPolicyContainerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 3),
    _RlLldpXMedLocMediaPolicyContainerVlanID_Type()
)
rlLldpXMedLocMediaPolicyContainerVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerVlanID.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerPriority_Type(Integer32):
    """Custom type rlLldpXMedLocMediaPolicyContainerPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlLldpXMedLocMediaPolicyContainerPriority_Type.__name__ = "Integer32"
_RlLldpXMedLocMediaPolicyContainerPriority_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerPriority = _RlLldpXMedLocMediaPolicyContainerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 4),
    _RlLldpXMedLocMediaPolicyContainerPriority_Type()
)
rlLldpXMedLocMediaPolicyContainerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerPriority.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerDscp_Type(Dscp):
    """Custom type rlLldpXMedLocMediaPolicyContainerDscp based on Dscp"""
    defaultValue = 0


_RlLldpXMedLocMediaPolicyContainerDscp_Type.__name__ = "Dscp"
_RlLldpXMedLocMediaPolicyContainerDscp_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerDscp = _RlLldpXMedLocMediaPolicyContainerDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 5),
    _RlLldpXMedLocMediaPolicyContainerDscp_Type()
)
rlLldpXMedLocMediaPolicyContainerDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerDscp.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerUnknown_Type(TruthValue):
    """Custom type rlLldpXMedLocMediaPolicyContainerUnknown based on TruthValue"""
    defaultValue = 2


_RlLldpXMedLocMediaPolicyContainerUnknown_Type.__name__ = "TruthValue"
_RlLldpXMedLocMediaPolicyContainerUnknown_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerUnknown = _RlLldpXMedLocMediaPolicyContainerUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 6),
    _RlLldpXMedLocMediaPolicyContainerUnknown_Type()
)
rlLldpXMedLocMediaPolicyContainerUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerUnknown.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerTagged_Type(TruthValue):
    """Custom type rlLldpXMedLocMediaPolicyContainerTagged based on TruthValue"""
    defaultValue = 2


_RlLldpXMedLocMediaPolicyContainerTagged_Type.__name__ = "TruthValue"
_RlLldpXMedLocMediaPolicyContainerTagged_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerTagged = _RlLldpXMedLocMediaPolicyContainerTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 7),
    _RlLldpXMedLocMediaPolicyContainerTagged_Type()
)
rlLldpXMedLocMediaPolicyContainerTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerTagged.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerPorts_Type(PortList):
    """Custom type rlLldpXMedLocMediaPolicyContainerPorts based on PortList"""
    defaultHexValue = ""


_RlLldpXMedLocMediaPolicyContainerPorts_Type.__name__ = "PortList"
_RlLldpXMedLocMediaPolicyContainerPorts_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerPorts = _RlLldpXMedLocMediaPolicyContainerPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 8),
    _RlLldpXMedLocMediaPolicyContainerPorts_Type()
)
rlLldpXMedLocMediaPolicyContainerPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerPorts.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerRowStatus_Type = RowStatus
_RlLldpXMedLocMediaPolicyContainerRowStatus_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerRowStatus = _RlLldpXMedLocMediaPolicyContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 1, 1, 9),
    _RlLldpXMedLocMediaPolicyContainerRowStatus_Type()
)
rlLldpXMedLocMediaPolicyContainerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerRowStatus.setStatus("current")
_RlLldpXMedNetPolVoiceUpdateMode_Type = PolicyAppVoiceUpdateMode
_RlLldpXMedNetPolVoiceUpdateMode_Object = MibScalar
rlLldpXMedNetPolVoiceUpdateMode = _RlLldpXMedNetPolVoiceUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 2, 2),
    _RlLldpXMedNetPolVoiceUpdateMode_Type()
)
rlLldpXMedNetPolVoiceUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedNetPolVoiceUpdateMode.setStatus("current")
_RlLldpTLVsTxOverload_ObjectIdentity = ObjectIdentity
rlLldpTLVsTxOverload = _RlLldpTLVsTxOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3)
)
_RlLldpTLVsTxOverloadingTable_Object = MibTable
rlLldpTLVsTxOverloadingTable = _RlLldpTLVsTxOverloadingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingTable.setStatus("current")
_RlLldpTLVsTxOverloadingEntry_Object = MibTableRow
rlLldpTLVsTxOverloadingEntry = _RlLldpTLVsTxOverloadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1)
)
rlLldpTLVsTxOverloadingEntry.setIndexNames(
    (0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingPortNum"),
    (0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingIndex"),
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingEntry.setStatus("current")
_RlLldpTxOverloadingPortNum_Type = LldpPortNumber
_RlLldpTxOverloadingPortNum_Object = MibTableColumn
rlLldpTxOverloadingPortNum = _RlLldpTxOverloadingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 1),
    _RlLldpTxOverloadingPortNum_Type()
)
rlLldpTxOverloadingPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingPortNum.setStatus("current")
_RlLldpTxOverloadingIndex_Type = Unsigned32
_RlLldpTxOverloadingIndex_Object = MibTableColumn
rlLldpTxOverloadingIndex = _RlLldpTxOverloadingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 2),
    _RlLldpTxOverloadingIndex_Type()
)
rlLldpTxOverloadingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingIndex.setStatus("current")


class _RlLldpTxOverloadingGroupId_Type(Integer32):
    """Custom type rlLldpTxOverloadingGroupId based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 1),
          ("optional", 2),
          ("medCap", 3),
          ("medLocation", 4),
          ("medNetPolicy", 5),
          ("medPoe", 6),
          ("medInventory", 7),
          ("xDot3", 8),
          ("xDot1", 9),
          ("dcbx", 10),
          ("cisco", 11))
    )


_RlLldpTxOverloadingGroupId_Type.__name__ = "Integer32"
_RlLldpTxOverloadingGroupId_Object = MibTableColumn
rlLldpTxOverloadingGroupId = _RlLldpTxOverloadingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 3),
    _RlLldpTxOverloadingGroupId_Type()
)
rlLldpTxOverloadingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingGroupId.setStatus("current")
_RlLldpTLVsTxSize_Type = Unsigned32
_RlLldpTLVsTxSize_Object = MibTableColumn
rlLldpTLVsTxSize = _RlLldpTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 4),
    _RlLldpTLVsTxSize_Type()
)
rlLldpTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxSize.setStatus("current")
_RlLldpTLVsTxGroupOverloading_Type = TruthValue
_RlLldpTLVsTxGroupOverloading_Object = MibTableColumn
rlLldpTLVsTxGroupOverloading = _RlLldpTLVsTxGroupOverloading_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 5),
    _RlLldpTLVsTxGroupOverloading_Type()
)
rlLldpTLVsTxGroupOverloading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxGroupOverloading.setStatus("current")
_RlLldpTLVsTxLeftSize_Type = Unsigned32
_RlLldpTLVsTxLeftSize_Object = MibTableColumn
rlLldpTLVsTxLeftSize = _RlLldpTLVsTxLeftSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 1, 1, 6),
    _RlLldpTLVsTxLeftSize_Type()
)
rlLldpTLVsTxLeftSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxLeftSize.setStatus("current")
_RlLldpTLVsTxOverloadingSizeTable_Object = MibTable
rlLldpTLVsTxOverloadingSizeTable = _RlLldpTLVsTxOverloadingSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingSizeTable.setStatus("current")
_RlLldpTLVsTxOverloadingSizeEntry_Object = MibTableRow
rlLldpTLVsTxOverloadingSizeEntry = _RlLldpTLVsTxOverloadingSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 2, 1)
)
rlLldpTLVsTxOverloadingSizeEntry.setIndexNames(
    (0, "CISCOSB-LLDP-MIB", "rlLldpTxOverloadingPortNum"),
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingSizeEntry.setStatus("current")
_RlLldpTotalTLVsTxSize_Type = Unsigned32
_RlLldpTotalTLVsTxSize_Object = MibTableColumn
rlLldpTotalTLVsTxSize = _RlLldpTotalTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 2, 1, 2),
    _RlLldpTotalTLVsTxSize_Type()
)
rlLldpTotalTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTotalTLVsTxSize.setStatus("current")
_RlLldpTLVsTxOverloading_Type = TruthValue
_RlLldpTLVsTxOverloading_Object = MibTableColumn
rlLldpTLVsTxOverloading = _RlLldpTLVsTxOverloading_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 2, 1, 3),
    _RlLldpTLVsTxOverloading_Type()
)
rlLldpTLVsTxOverloading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloading.setStatus("current")
_RlLldpLeftTLVsTxSize_Type = Unsigned32
_RlLldpLeftTLVsTxSize_Object = MibTableColumn
rlLldpLeftTLVsTxSize = _RlLldpLeftTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 2, 1, 4),
    _RlLldpLeftTLVsTxSize_Type()
)
rlLldpLeftTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLeftTLVsTxSize.setStatus("current")
_RlLldpTLVsTxOverloadingPorts_Type = PortList
_RlLldpTLVsTxOverloadingPorts_Object = MibScalar
rlLldpTLVsTxOverloadingPorts = _RlLldpTLVsTxOverloadingPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 3, 3),
    _RlLldpTLVsTxOverloadingPorts_Type()
)
rlLldpTLVsTxOverloadingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingPorts.setStatus("current")
_RlLldpRemStatus_ObjectIdentity = ObjectIdentity
rlLldpRemStatus = _RlLldpRemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4)
)
_RlLldpRemTtlTable_Object = MibTable
rlLldpRemTtlTable = _RlLldpRemTtlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rlLldpRemTtlTable.setStatus("current")
_RlLldpRemTtlEntry_Object = MibTableRow
rlLldpRemTtlEntry = _RlLldpRemTtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1, 1)
)
rlLldpRemTtlEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    rlLldpRemTtlEntry.setStatus("current")
_RlLldpRemTtl_Type = Unsigned32
_RlLldpRemTtl_Object = MibTableColumn
rlLldpRemTtl = _RlLldpRemTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 4, 1, 1, 1),
    _RlLldpRemTtl_Type()
)
rlLldpRemTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRemTtl.setStatus("current")
if mibBuilder.loadTexts:
    rlLldpRemTtl.setUnits("seconds")
_RlLldpLocalSystemData_ObjectIdentity = ObjectIdentity
rlLldpLocalSystemData = _RlLldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5)
)
_RlLldpLoc4WirePowerTable_Object = MibTable
rlLldpLoc4WirePowerTable = _RlLldpLoc4WirePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerTable.setStatus("current")
_RlLldpLoc4WirePowerEntry_Object = MibTableRow
rlLldpLoc4WirePowerEntry = _RlLldpLoc4WirePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1, 1)
)
rlLldpLoc4WirePowerEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerEntry.setStatus("current")
_RlLldpLoc4WirePowerSupported_Type = TruthValue
_RlLldpLoc4WirePowerSupported_Object = MibTableColumn
rlLldpLoc4WirePowerSupported = _RlLldpLoc4WirePowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1, 1, 1),
    _RlLldpLoc4WirePowerSupported_Type()
)
rlLldpLoc4WirePowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerSupported.setStatus("current")
_RlLldpLoc4WirePowerSpPairDetClasReq_Type = TruthValue
_RlLldpLoc4WirePowerSpPairDetClasReq_Object = MibTableColumn
rlLldpLoc4WirePowerSpPairDetClasReq = _RlLldpLoc4WirePowerSpPairDetClasReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1, 1, 2),
    _RlLldpLoc4WirePowerSpPairDetClasReq_Type()
)
rlLldpLoc4WirePowerSpPairDetClasReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerSpPairDetClasReq.setStatus("current")
_RlLldpLoc4WirePowerPdSpPairDesStEn_Type = TruthValue
_RlLldpLoc4WirePowerPdSpPairDesStEn_Object = MibTableColumn
rlLldpLoc4WirePowerPdSpPairDesStEn = _RlLldpLoc4WirePowerPdSpPairDesStEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1, 1, 3),
    _RlLldpLoc4WirePowerPdSpPairDesStEn_Type()
)
rlLldpLoc4WirePowerPdSpPairDesStEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerPdSpPairDesStEn.setStatus("current")
_RlLldpLoc4WirePowerPseSpPairOpStEn_Type = TruthValue
_RlLldpLoc4WirePowerPseSpPairOpStEn_Object = MibTableColumn
rlLldpLoc4WirePowerPseSpPairOpStEn = _RlLldpLoc4WirePowerPseSpPairOpStEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 5, 1, 1, 4),
    _RlLldpLoc4WirePowerPseSpPairOpStEn_Type()
)
rlLldpLoc4WirePowerPseSpPairOpStEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLoc4WirePowerPseSpPairOpStEn.setStatus("current")
_RlLldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
rlLldpRemoteSystemsData = _RlLldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6)
)
_RlLldpRem4WirePowerTable_Object = MibTable
rlLldpRem4WirePowerTable = _RlLldpRem4WirePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerTable.setStatus("current")
_RlLldpRem4WirePowerEntry_Object = MibTableRow
rlLldpRem4WirePowerEntry = _RlLldpRem4WirePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1, 1)
)
rlLldpRem4WirePowerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerEntry.setStatus("current")
_RlLldpRem4WirePowerSupported_Type = TruthValue
_RlLldpRem4WirePowerSupported_Object = MibTableColumn
rlLldpRem4WirePowerSupported = _RlLldpRem4WirePowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1, 1, 1),
    _RlLldpRem4WirePowerSupported_Type()
)
rlLldpRem4WirePowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerSupported.setStatus("current")
_RlLldpRem4WirePowerSpPairDetClasReq_Type = TruthValue
_RlLldpRem4WirePowerSpPairDetClasReq_Object = MibTableColumn
rlLldpRem4WirePowerSpPairDetClasReq = _RlLldpRem4WirePowerSpPairDetClasReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1, 1, 2),
    _RlLldpRem4WirePowerSpPairDetClasReq_Type()
)
rlLldpRem4WirePowerSpPairDetClasReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerSpPairDetClasReq.setStatus("current")
_RlLldpRem4WirePowerPdSpPairDesStEn_Type = TruthValue
_RlLldpRem4WirePowerPdSpPairDesStEn_Object = MibTableColumn
rlLldpRem4WirePowerPdSpPairDesStEn = _RlLldpRem4WirePowerPdSpPairDesStEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1, 1, 3),
    _RlLldpRem4WirePowerPdSpPairDesStEn_Type()
)
rlLldpRem4WirePowerPdSpPairDesStEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerPdSpPairDesStEn.setStatus("current")
_RlLldpRem4WirePowerPseSpPairOpStEn_Type = TruthValue
_RlLldpRem4WirePowerPseSpPairOpStEn_Object = MibTableColumn
rlLldpRem4WirePowerPseSpPairOpStEn = _RlLldpRem4WirePowerPseSpPairOpStEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110, 1, 6, 1, 1, 4),
    _RlLldpRem4WirePowerPseSpPairOpStEn_Type()
)
rlLldpRem4WirePowerPseSpPairOpStEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRem4WirePowerPseSpPairOpStEn.setStatus("current")
lldpPortConfigEntry.registerAugmentions(
    ("CISCOSB-LLDP-MIB",
     "rlLldpPortConfigEntry")
)
rlLldpPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rlLldpTLVsTxOverloadingStateEnterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 209)
)
rlLldpTLVsTxOverloadingStateEnterTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingStateEnterTrap.setStatus(
        "current"
    )

rlLldpTLVsTxOverloadingStateExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 210)
)
rlLldpTLVsTxOverloadingStateExitTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingStateExitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-LLDP-MIB",
    **{"PolicyNumber": PolicyNumber,
       "PolicyContainerAppType": PolicyContainerAppType,
       "PolicyAppVoiceUpdateMode": PolicyAppVoiceUpdateMode,
       "rlLldpTLVsTxOverloadingStateEnterTrap": rlLldpTLVsTxOverloadingStateEnterTrap,
       "rlLldpTLVsTxOverloadingStateExitTrap": rlLldpTLVsTxOverloadingStateExitTrap,
       "rlLldp": rlLldp,
       "rlLldpObjects": rlLldpObjects,
       "rlLldpConfig": rlLldpConfig,
       "rlLldpEnabled": rlLldpEnabled,
       "rlLldpClearRx": rlLldpClearRx,
       "rlLldpDuMode": rlLldpDuMode,
       "rlLldpAutoAdvLocPortManAddrTable": rlLldpAutoAdvLocPortManAddrTable,
       "rlLldpAutoAdvLocPortManAddrEntry": rlLldpAutoAdvLocPortManAddrEntry,
       "rlLldpAutoAdvLocPortNum": rlLldpAutoAdvLocPortNum,
       "rlLldpAutoAdvManAddrOwnerIfId": rlLldpAutoAdvManAddrOwnerIfId,
       "rlLldpAutoAdvManAddrNone": rlLldpAutoAdvManAddrNone,
       "rlLldpAutoAdvManAddrSubtype": rlLldpAutoAdvManAddrSubtype,
       "rlLldpAutoAdvManAddr": rlLldpAutoAdvManAddr,
       "rlLldpAutoAdvPortsStatus": rlLldpAutoAdvPortsStatus,
       "rlLldpChassisIdSubtype": rlLldpChassisIdSubtype,
       "rlLldpPortConfigTable": rlLldpPortConfigTable,
       "rlLldpPortConfigEntry": rlLldpPortConfigEntry,
       "rlLldpPortConfig4wireTxEnable": rlLldpPortConfig4wireTxEnable,
       "rlLldpXMedConfig": rlLldpXMedConfig,
       "rlLldpXMedLocMediaPolicyContainerTable": rlLldpXMedLocMediaPolicyContainerTable,
       "rlLldpXMedLocMediaPolicyContainerEntry": rlLldpXMedLocMediaPolicyContainerEntry,
       "rlLldpXMedLocMediaPolicyContainerIndex": rlLldpXMedLocMediaPolicyContainerIndex,
       "rlLldpXMedLocMediaPolicyContainerAppType": rlLldpXMedLocMediaPolicyContainerAppType,
       "rlLldpXMedLocMediaPolicyContainerVlanID": rlLldpXMedLocMediaPolicyContainerVlanID,
       "rlLldpXMedLocMediaPolicyContainerPriority": rlLldpXMedLocMediaPolicyContainerPriority,
       "rlLldpXMedLocMediaPolicyContainerDscp": rlLldpXMedLocMediaPolicyContainerDscp,
       "rlLldpXMedLocMediaPolicyContainerUnknown": rlLldpXMedLocMediaPolicyContainerUnknown,
       "rlLldpXMedLocMediaPolicyContainerTagged": rlLldpXMedLocMediaPolicyContainerTagged,
       "rlLldpXMedLocMediaPolicyContainerPorts": rlLldpXMedLocMediaPolicyContainerPorts,
       "rlLldpXMedLocMediaPolicyContainerRowStatus": rlLldpXMedLocMediaPolicyContainerRowStatus,
       "rlLldpXMedNetPolVoiceUpdateMode": rlLldpXMedNetPolVoiceUpdateMode,
       "rlLldpTLVsTxOverload": rlLldpTLVsTxOverload,
       "rlLldpTLVsTxOverloadingTable": rlLldpTLVsTxOverloadingTable,
       "rlLldpTLVsTxOverloadingEntry": rlLldpTLVsTxOverloadingEntry,
       "rlLldpTxOverloadingPortNum": rlLldpTxOverloadingPortNum,
       "rlLldpTxOverloadingIndex": rlLldpTxOverloadingIndex,
       "rlLldpTxOverloadingGroupId": rlLldpTxOverloadingGroupId,
       "rlLldpTLVsTxSize": rlLldpTLVsTxSize,
       "rlLldpTLVsTxGroupOverloading": rlLldpTLVsTxGroupOverloading,
       "rlLldpTLVsTxLeftSize": rlLldpTLVsTxLeftSize,
       "rlLldpTLVsTxOverloadingSizeTable": rlLldpTLVsTxOverloadingSizeTable,
       "rlLldpTLVsTxOverloadingSizeEntry": rlLldpTLVsTxOverloadingSizeEntry,
       "rlLldpTotalTLVsTxSize": rlLldpTotalTLVsTxSize,
       "rlLldpTLVsTxOverloading": rlLldpTLVsTxOverloading,
       "rlLldpLeftTLVsTxSize": rlLldpLeftTLVsTxSize,
       "rlLldpTLVsTxOverloadingPorts": rlLldpTLVsTxOverloadingPorts,
       "rlLldpRemStatus": rlLldpRemStatus,
       "rlLldpRemTtlTable": rlLldpRemTtlTable,
       "rlLldpRemTtlEntry": rlLldpRemTtlEntry,
       "rlLldpRemTtl": rlLldpRemTtl,
       "rlLldpLocalSystemData": rlLldpLocalSystemData,
       "rlLldpLoc4WirePowerTable": rlLldpLoc4WirePowerTable,
       "rlLldpLoc4WirePowerEntry": rlLldpLoc4WirePowerEntry,
       "rlLldpLoc4WirePowerSupported": rlLldpLoc4WirePowerSupported,
       "rlLldpLoc4WirePowerSpPairDetClasReq": rlLldpLoc4WirePowerSpPairDetClasReq,
       "rlLldpLoc4WirePowerPdSpPairDesStEn": rlLldpLoc4WirePowerPdSpPairDesStEn,
       "rlLldpLoc4WirePowerPseSpPairOpStEn": rlLldpLoc4WirePowerPseSpPairOpStEn,
       "rlLldpRemoteSystemsData": rlLldpRemoteSystemsData,
       "rlLldpRem4WirePowerTable": rlLldpRem4WirePowerTable,
       "rlLldpRem4WirePowerEntry": rlLldpRem4WirePowerEntry,
       "rlLldpRem4WirePowerSupported": rlLldpRem4WirePowerSupported,
       "rlLldpRem4WirePowerSpPairDetClasReq": rlLldpRem4WirePowerSpPairDetClasReq,
       "rlLldpRem4WirePowerPdSpPairDesStEn": rlLldpRem4WirePowerPdSpPairDesStEn,
       "rlLldpRem4WirePowerPseSpPairOpStEn": rlLldpRem4WirePowerPseSpPairOpStEn}
)
