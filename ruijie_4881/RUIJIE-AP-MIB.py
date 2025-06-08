# SNMP MIB module (RUIJIE-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex",
    "MemberMap")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7)
)
if mibBuilder.loadTexts:
    ruijieApMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieApMIBObjects_ObjectIdentity = ObjectIdentity
ruijieApMIBObjects = _RuijieApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1)
)
_RuijieApMaxNumber_Type = Integer32
_RuijieApMaxNumber_Object = MibScalar
ruijieApMaxNumber = _RuijieApMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 1),
    _RuijieApMaxNumber_Type()
)
ruijieApMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMaxNumber.setStatus("current")
_RuijieApCurrentNumber_Type = Integer32
_RuijieApCurrentNumber_Object = MibScalar
ruijieApCurrentNumber = _RuijieApCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 2),
    _RuijieApCurrentNumber_Type()
)
ruijieApCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApCurrentNumber.setStatus("current")
_RuijieApPortConfigTable_Object = MibTable
ruijieApPortConfigTable = _RuijieApPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieApPortConfigTable.setStatus("obsolete")
_RuijieApPortConfigEntry_Object = MibTableRow
ruijieApPortConfigEntry = _RuijieApPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 3, 1)
)
ruijieApPortConfigEntry.setIndexNames(
    (0, "RUIJIE-AP-MIB", "ruijieApPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieApPortConfigEntry.setStatus("obsolete")
_RuijieApPortConfigPortIndex_Type = IfIndex
_RuijieApPortConfigPortIndex_Object = MibTableColumn
ruijieApPortConfigPortIndex = _RuijieApPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 3, 1, 1),
    _RuijieApPortConfigPortIndex_Type()
)
ruijieApPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApPortConfigPortIndex.setStatus("obsolete")
_RuijieApPortConfigApIndex_Type = IfIndex
_RuijieApPortConfigApIndex_Object = MibTableColumn
ruijieApPortConfigApIndex = _RuijieApPortConfigApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 3, 1, 2),
    _RuijieApPortConfigApIndex_Type()
)
ruijieApPortConfigApIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApPortConfigApIndex.setStatus("obsolete")
_RuijieApTable_Object = MibTable
ruijieApTable = _RuijieApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieApTable.setStatus("obsolete")
_RuijieApEntry_Object = MibTableRow
ruijieApEntry = _RuijieApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4, 1)
)
ruijieApEntry.setIndexNames(
    (0, "RUIJIE-AP-MIB", "ruijieApIndex"),
)
if mibBuilder.loadTexts:
    ruijieApEntry.setStatus("obsolete")
_RuijieApIndex_Type = IfIndex
_RuijieApIndex_Object = MibTableColumn
ruijieApIndex = _RuijieApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4, 1, 1),
    _RuijieApIndex_Type()
)
ruijieApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIndex.setStatus("obsolete")
_RuijieApMemberAction_Type = MemberMap
_RuijieApMemberAction_Object = MibTableColumn
ruijieApMemberAction = _RuijieApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4, 1, 2),
    _RuijieApMemberAction_Type()
)
ruijieApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMemberAction.setStatus("obsolete")
_RuijieApPossibleMember_Type = MemberMap
_RuijieApPossibleMember_Object = MibTableColumn
ruijieApPossibleMember = _RuijieApPossibleMember_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4, 1, 3),
    _RuijieApPossibleMember_Type()
)
ruijieApPossibleMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPossibleMember.setStatus("obsolete")
_RuijieApMaxPtNumber_Type = Integer32
_RuijieApMaxPtNumber_Object = MibTableColumn
ruijieApMaxPtNumber = _RuijieApMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 4, 1, 4),
    _RuijieApMaxPtNumber_Type()
)
ruijieApMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMaxPtNumber.setStatus("obsolete")


class _RuijieApFlowBalance_Type(Integer32):
    """Custom type ruijieApFlowBalance based on Integer32"""
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
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("source-mac", 1),
          ("destination-mac", 2),
          ("src-dest-mac", 3),
          ("source-ip", 4),
          ("destination-ip", 5),
          ("src-dest-ip", 6),
          ("src-dest-port", 7),
          ("src-dst-ip-l4port", 8),
          ("enhanced-profile", 9),
          ("src-l4port", 10),
          ("dest-l4port", 11),
          ("src-dest-l4port", 12),
          ("src-ip-l4port", 13),
          ("dest-ip-l4port", 14),
          ("src-ip-dest-l4port", 15),
          ("dest-ip-src-l4port", 16),
          ("src-dest-ip-src-l4port", 17),
          ("src-dest-ip-dest-l4port", 18),
          ("src-ip-src-dest-l4port", 19),
          ("dest-ip-src-dest-l4port", 20))
    )


_RuijieApFlowBalance_Type.__name__ = "Integer32"
_RuijieApFlowBalance_Object = MibScalar
ruijieApFlowBalance = _RuijieApFlowBalance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 5),
    _RuijieApFlowBalance_Type()
)
ruijieApFlowBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApFlowBalance.setStatus("current")
_RuijieApConfigTable_Object = MibTable
ruijieApConfigTable = _RuijieApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieApConfigTable.setStatus("current")
_RuijieApConfigEntry_Object = MibTableRow
ruijieApConfigEntry = _RuijieApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1)
)
ruijieApConfigEntry.setIndexNames(
    (0, "RUIJIE-AP-MIB", "ruijieApConfigNumber"),
)
if mibBuilder.loadTexts:
    ruijieApConfigEntry.setStatus("current")
_RuijieApConfigNumber_Type = Integer32
_RuijieApConfigNumber_Object = MibTableColumn
ruijieApConfigNumber = _RuijieApConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 1),
    _RuijieApConfigNumber_Type()
)
ruijieApConfigNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApConfigNumber.setStatus("current")
_RuijieApConfigIndex_Type = IfIndex
_RuijieApConfigIndex_Object = MibTableColumn
ruijieApConfigIndex = _RuijieApConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 2),
    _RuijieApConfigIndex_Type()
)
ruijieApConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApConfigIndex.setStatus("current")
_RuijieApConfigMaxPtNumber_Type = Integer32
_RuijieApConfigMaxPtNumber_Object = MibTableColumn
ruijieApConfigMaxPtNumber = _RuijieApConfigMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 3),
    _RuijieApConfigMaxPtNumber_Type()
)
ruijieApConfigMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApConfigMaxPtNumber.setStatus("current")
_RuijieApConfigCurrentPtNumber_Type = Integer32
_RuijieApConfigCurrentPtNumber_Object = MibTableColumn
ruijieApConfigCurrentPtNumber = _RuijieApConfigCurrentPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 4),
    _RuijieApConfigCurrentPtNumber_Type()
)
ruijieApConfigCurrentPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApConfigCurrentPtNumber.setStatus("current")
_RuijieApConfigPortMember_Type = PortList
_RuijieApConfigPortMember_Object = MibTableColumn
ruijieApConfigPortMember = _RuijieApConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 5),
    _RuijieApConfigPortMember_Type()
)
ruijieApConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApConfigPortMember.setStatus("current")
_RuijieApConfigAction_Type = Integer32
_RuijieApConfigAction_Object = MibTableColumn
ruijieApConfigAction = _RuijieApConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 6, 1, 6),
    _RuijieApConfigAction_Type()
)
ruijieApConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApConfigAction.setStatus("current")
_RuijieApPortMemberTable_Object = MibTable
ruijieApPortMemberTable = _RuijieApPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieApPortMemberTable.setStatus("current")
_RuijieApPortMemberEntry_Object = MibTableRow
ruijieApPortMemberEntry = _RuijieApPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7, 1)
)
ruijieApPortMemberEntry.setIndexNames(
    (0, "RUIJIE-AP-MIB", "ruijieApPortMemberPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieApPortMemberEntry.setStatus("current")
_RuijieApPortMemberPortIndex_Type = IfIndex
_RuijieApPortMemberPortIndex_Object = MibTableColumn
ruijieApPortMemberPortIndex = _RuijieApPortMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7, 1, 1),
    _RuijieApPortMemberPortIndex_Type()
)
ruijieApPortMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPortMemberPortIndex.setStatus("current")
_RuijieApPortMemberApNumber_Type = Integer32
_RuijieApPortMemberApNumber_Object = MibTableColumn
ruijieApPortMemberApNumber = _RuijieApPortMemberApNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7, 1, 2),
    _RuijieApPortMemberApNumber_Type()
)
ruijieApPortMemberApNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApPortMemberApNumber.setStatus("current")
_RuijieApPortMemberAction_Type = Integer32
_RuijieApPortMemberAction_Object = MibTableColumn
ruijieApPortMemberAction = _RuijieApPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7, 1, 3),
    _RuijieApPortMemberAction_Type()
)
ruijieApPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApPortMemberAction.setStatus("current")


class _RuijieApPortMemberLacpStatus_Type(Integer32):
    """Custom type ruijieApPortMemberLacpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-lacp-member", 0),
          ("down", 1),
          ("bndl", 2),
          ("susp", 3),
          ("individual", 4))
    )


_RuijieApPortMemberLacpStatus_Type.__name__ = "Integer32"
_RuijieApPortMemberLacpStatus_Object = MibTableColumn
ruijieApPortMemberLacpStatus = _RuijieApPortMemberLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 7, 1, 4),
    _RuijieApPortMemberLacpStatus_Type()
)
ruijieApPortMemberLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPortMemberLacpStatus.setStatus("current")
_RuijieApBalcProfName_Type = DisplayString
_RuijieApBalcProfName_Object = MibScalar
ruijieApBalcProfName = _RuijieApBalcProfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 8),
    _RuijieApBalcProfName_Type()
)
ruijieApBalcProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApBalcProfName.setStatus("current")
_RuijieApProfTable_Object = MibTable
ruijieApProfTable = _RuijieApProfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieApProfTable.setStatus("current")
_RuijieApProfEntry_Object = MibTableRow
ruijieApProfEntry = _RuijieApProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1)
)
ruijieApProfEntry.setIndexNames(
    (0, "RUIJIE-AP-MIB", "ruijieApProfIdx"),
)
if mibBuilder.loadTexts:
    ruijieApProfEntry.setStatus("current")
_RuijieApProfIdx_Type = Integer32
_RuijieApProfIdx_Object = MibTableColumn
ruijieApProfIdx = _RuijieApProfIdx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 1),
    _RuijieApProfIdx_Type()
)
ruijieApProfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApProfIdx.setStatus("current")
_RuijieApProfName_Type = DisplayString
_RuijieApProfName_Object = MibTableColumn
ruijieApProfName = _RuijieApProfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 2),
    _RuijieApProfName_Type()
)
ruijieApProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApProfName.setStatus("current")
_RuijieApProfL2SrcMac_Type = TruthValue
_RuijieApProfL2SrcMac_Object = MibTableColumn
ruijieApProfL2SrcMac = _RuijieApProfL2SrcMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 3),
    _RuijieApProfL2SrcMac_Type()
)
ruijieApProfL2SrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfL2SrcMac.setStatus("current")
_RuijieApProfL2DestMac_Type = TruthValue
_RuijieApProfL2DestMac_Object = MibTableColumn
ruijieApProfL2DestMac = _RuijieApProfL2DestMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 4),
    _RuijieApProfL2DestMac_Type()
)
ruijieApProfL2DestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfL2DestMac.setStatus("current")
_RuijieApProfL2Pro_Type = TruthValue
_RuijieApProfL2Pro_Object = MibTableColumn
ruijieApProfL2Pro = _RuijieApProfL2Pro_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 5),
    _RuijieApProfL2Pro_Type()
)
ruijieApProfL2Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfL2Pro.setStatus("current")
_RuijieApProfL2Vlan_Type = TruthValue
_RuijieApProfL2Vlan_Object = MibTableColumn
ruijieApProfL2Vlan = _RuijieApProfL2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 6),
    _RuijieApProfL2Vlan_Type()
)
ruijieApProfL2Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfL2Vlan.setStatus("current")
_RuijieApProfL2SrcPort_Type = TruthValue
_RuijieApProfL2SrcPort_Object = MibTableColumn
ruijieApProfL2SrcPort = _RuijieApProfL2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 7),
    _RuijieApProfL2SrcPort_Type()
)
ruijieApProfL2SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfL2SrcPort.setStatus("current")
_RuijieApProfIpv4SrcIp_Type = TruthValue
_RuijieApProfIpv4SrcIp_Object = MibTableColumn
ruijieApProfIpv4SrcIp = _RuijieApProfIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 8),
    _RuijieApProfIpv4SrcIp_Type()
)
ruijieApProfIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4SrcIp.setStatus("current")
_RuijieApProfIpv4DestIp_Type = TruthValue
_RuijieApProfIpv4DestIp_Object = MibTableColumn
ruijieApProfIpv4DestIp = _RuijieApProfIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 9),
    _RuijieApProfIpv4DestIp_Type()
)
ruijieApProfIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4DestIp.setStatus("current")
_RuijieApProfIpv4Pro_Type = TruthValue
_RuijieApProfIpv4Pro_Object = MibTableColumn
ruijieApProfIpv4Pro = _RuijieApProfIpv4Pro_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 10),
    _RuijieApProfIpv4Pro_Type()
)
ruijieApProfIpv4Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4Pro.setStatus("current")
_RuijieApProfIpv4L4SrcPort_Type = TruthValue
_RuijieApProfIpv4L4SrcPort_Object = MibTableColumn
ruijieApProfIpv4L4SrcPort = _RuijieApProfIpv4L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 11),
    _RuijieApProfIpv4L4SrcPort_Type()
)
ruijieApProfIpv4L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4L4SrcPort.setStatus("current")
_RuijieApProfIpv4L4DestPort_Type = TruthValue
_RuijieApProfIpv4L4DestPort_Object = MibTableColumn
ruijieApProfIpv4L4DestPort = _RuijieApProfIpv4L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 12),
    _RuijieApProfIpv4L4DestPort_Type()
)
ruijieApProfIpv4L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4L4DestPort.setStatus("current")
_RuijieApProfIpv4Vlan_Type = TruthValue
_RuijieApProfIpv4Vlan_Object = MibTableColumn
ruijieApProfIpv4Vlan = _RuijieApProfIpv4Vlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 13),
    _RuijieApProfIpv4Vlan_Type()
)
ruijieApProfIpv4Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4Vlan.setStatus("current")
_RuijieApProfIpv4SrcPort_Type = TruthValue
_RuijieApProfIpv4SrcPort_Object = MibTableColumn
ruijieApProfIpv4SrcPort = _RuijieApProfIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 14),
    _RuijieApProfIpv4SrcPort_Type()
)
ruijieApProfIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv4SrcPort.setStatus("current")
_RuijieApProfIpv6SrcIp_Type = TruthValue
_RuijieApProfIpv6SrcIp_Object = MibTableColumn
ruijieApProfIpv6SrcIp = _RuijieApProfIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 15),
    _RuijieApProfIpv6SrcIp_Type()
)
ruijieApProfIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6SrcIp.setStatus("current")
_RuijieApProfIpv6DestIp_Type = TruthValue
_RuijieApProfIpv6DestIp_Object = MibTableColumn
ruijieApProfIpv6DestIp = _RuijieApProfIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 16),
    _RuijieApProfIpv6DestIp_Type()
)
ruijieApProfIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6DestIp.setStatus("current")
_RuijieApProfIpv6Pro_Type = TruthValue
_RuijieApProfIpv6Pro_Object = MibTableColumn
ruijieApProfIpv6Pro = _RuijieApProfIpv6Pro_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 17),
    _RuijieApProfIpv6Pro_Type()
)
ruijieApProfIpv6Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6Pro.setStatus("current")
_RuijieApProfIpv6L4SrcPort_Type = TruthValue
_RuijieApProfIpv6L4SrcPort_Object = MibTableColumn
ruijieApProfIpv6L4SrcPort = _RuijieApProfIpv6L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 18),
    _RuijieApProfIpv6L4SrcPort_Type()
)
ruijieApProfIpv6L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6L4SrcPort.setStatus("current")
_RuijieApProfIpv6L4DestPort_Type = TruthValue
_RuijieApProfIpv6L4DestPort_Object = MibTableColumn
ruijieApProfIpv6L4DestPort = _RuijieApProfIpv6L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 19),
    _RuijieApProfIpv6L4DestPort_Type()
)
ruijieApProfIpv6L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6L4DestPort.setStatus("current")
_RuijieApProfIpv6Vlan_Type = TruthValue
_RuijieApProfIpv6Vlan_Object = MibTableColumn
ruijieApProfIpv6Vlan = _RuijieApProfIpv6Vlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 20),
    _RuijieApProfIpv6Vlan_Type()
)
ruijieApProfIpv6Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6Vlan.setStatus("current")
_RuijieApProfIpv6SrcPort_Type = TruthValue
_RuijieApProfIpv6SrcPort_Object = MibTableColumn
ruijieApProfIpv6SrcPort = _RuijieApProfIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 21),
    _RuijieApProfIpv6SrcPort_Type()
)
ruijieApProfIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfIpv6SrcPort.setStatus("current")
_RuijieApProfMplsTopLabel_Type = TruthValue
_RuijieApProfMplsTopLabel_Object = MibTableColumn
ruijieApProfMplsTopLabel = _RuijieApProfMplsTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 22),
    _RuijieApProfMplsTopLabel_Type()
)
ruijieApProfMplsTopLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMplsTopLabel.setStatus("current")
_RuijieApProfMpls2ndLabel_Type = TruthValue
_RuijieApProfMpls2ndLabel_Object = MibTableColumn
ruijieApProfMpls2ndLabel = _RuijieApProfMpls2ndLabel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 23),
    _RuijieApProfMpls2ndLabel_Type()
)
ruijieApProfMpls2ndLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMpls2ndLabel.setStatus("current")
_RuijieApProfMplsSrcIp_Type = TruthValue
_RuijieApProfMplsSrcIp_Object = MibTableColumn
ruijieApProfMplsSrcIp = _RuijieApProfMplsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 24),
    _RuijieApProfMplsSrcIp_Type()
)
ruijieApProfMplsSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMplsSrcIp.setStatus("current")
_RuijieApProfMplsDestIp_Type = TruthValue
_RuijieApProfMplsDestIp_Object = MibTableColumn
ruijieApProfMplsDestIp = _RuijieApProfMplsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 25),
    _RuijieApProfMplsDestIp_Type()
)
ruijieApProfMplsDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMplsDestIp.setStatus("current")
_RuijieApProfMplsVlan_Type = TruthValue
_RuijieApProfMplsVlan_Object = MibTableColumn
ruijieApProfMplsVlan = _RuijieApProfMplsVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 26),
    _RuijieApProfMplsVlan_Type()
)
ruijieApProfMplsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMplsVlan.setStatus("current")
_RuijieApProfMplsSrcPort_Type = TruthValue
_RuijieApProfMplsSrcPort_Object = MibTableColumn
ruijieApProfMplsSrcPort = _RuijieApProfMplsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 1, 9, 1, 27),
    _RuijieApProfMplsSrcPort_Type()
)
ruijieApProfMplsSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApProfMplsSrcPort.setStatus("current")
_RuijieApMIBConformance_ObjectIdentity = ObjectIdentity
ruijieApMIBConformance = _RuijieApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 2)
)
_RuijieApMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieApMIBCompliances = _RuijieApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 2, 1)
)
_RuijieApMIBGroups_ObjectIdentity = ObjectIdentity
ruijieApMIBGroups = _RuijieApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 2, 2)
)

# Managed Objects groups

ruijieApMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 2, 2, 1)
)
ruijieApMIBGroup.setObjects(
      *(("RUIJIE-AP-MIB", "ruijieApMaxNumber"),
        ("RUIJIE-AP-MIB", "ruijieApCurrentNumber"),
        ("RUIJIE-AP-MIB", "ruijieApPortConfigApIndex"),
        ("RUIJIE-AP-MIB", "ruijieApIndex"),
        ("RUIJIE-AP-MIB", "ruijieApMemberAction"),
        ("RUIJIE-AP-MIB", "ruijieApMaxPtNumber"),
        ("RUIJIE-AP-MIB", "ruijieApFlowBalance"),
        ("RUIJIE-AP-MIB", "ruijieApConfigNumber"),
        ("RUIJIE-AP-MIB", "ruijieApConfigIndex"),
        ("RUIJIE-AP-MIB", "ruijieApConfigMaxPtNumber"),
        ("RUIJIE-AP-MIB", "ruijieApConfigCurrentPtNumber"),
        ("RUIJIE-AP-MIB", "ruijieApConfigPortMember"),
        ("RUIJIE-AP-MIB", "ruijieApConfigAction"),
        ("RUIJIE-AP-MIB", "ruijieApPortMemberPortIndex"),
        ("RUIJIE-AP-MIB", "ruijieApPortMemberApNumber"),
        ("RUIJIE-AP-MIB", "ruijieApPortMemberAction"),
        ("RUIJIE-AP-MIB", "ruijieApPortMemberLacpStatus"),
        ("RUIJIE-AP-MIB", "ruijieApProfL2SrcMac"),
        ("RUIJIE-AP-MIB", "ruijieApProfL2DestMac"),
        ("RUIJIE-AP-MIB", "ruijieApProfL2Pro"),
        ("RUIJIE-AP-MIB", "ruijieApProfL2Vlan"),
        ("RUIJIE-AP-MIB", "ruijieApProfL2SrcPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4SrcIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4DestIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4Pro"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4L4SrcPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4L4DestPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4Vlan"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv4SrcPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6SrcIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6DestIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6Pro"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6L4SrcPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6L4DestPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6Vlan"),
        ("RUIJIE-AP-MIB", "ruijieApProfIpv6SrcPort"),
        ("RUIJIE-AP-MIB", "ruijieApProfMplsTopLabel"),
        ("RUIJIE-AP-MIB", "ruijieApProfMpls2ndLabel"),
        ("RUIJIE-AP-MIB", "ruijieApProfMplsSrcIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfMplsDestIp"),
        ("RUIJIE-AP-MIB", "ruijieApProfMplsVlan"),
        ("RUIJIE-AP-MIB", "ruijieApProfMplsSrcPort"))
)
if mibBuilder.loadTexts:
    ruijieApMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 7, 2, 1, 1)
)
ruijieApMIBCompliance.setObjects(
    ("RUIJIE-AP-MIB", "ruijieApMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieApMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AP-MIB",
    **{"ruijieApMIB": ruijieApMIB,
       "ruijieApMIBObjects": ruijieApMIBObjects,
       "ruijieApMaxNumber": ruijieApMaxNumber,
       "ruijieApCurrentNumber": ruijieApCurrentNumber,
       "ruijieApPortConfigTable": ruijieApPortConfigTable,
       "ruijieApPortConfigEntry": ruijieApPortConfigEntry,
       "ruijieApPortConfigPortIndex": ruijieApPortConfigPortIndex,
       "ruijieApPortConfigApIndex": ruijieApPortConfigApIndex,
       "ruijieApTable": ruijieApTable,
       "ruijieApEntry": ruijieApEntry,
       "ruijieApIndex": ruijieApIndex,
       "ruijieApMemberAction": ruijieApMemberAction,
       "ruijieApPossibleMember": ruijieApPossibleMember,
       "ruijieApMaxPtNumber": ruijieApMaxPtNumber,
       "ruijieApFlowBalance": ruijieApFlowBalance,
       "ruijieApConfigTable": ruijieApConfigTable,
       "ruijieApConfigEntry": ruijieApConfigEntry,
       "ruijieApConfigNumber": ruijieApConfigNumber,
       "ruijieApConfigIndex": ruijieApConfigIndex,
       "ruijieApConfigMaxPtNumber": ruijieApConfigMaxPtNumber,
       "ruijieApConfigCurrentPtNumber": ruijieApConfigCurrentPtNumber,
       "ruijieApConfigPortMember": ruijieApConfigPortMember,
       "ruijieApConfigAction": ruijieApConfigAction,
       "ruijieApPortMemberTable": ruijieApPortMemberTable,
       "ruijieApPortMemberEntry": ruijieApPortMemberEntry,
       "ruijieApPortMemberPortIndex": ruijieApPortMemberPortIndex,
       "ruijieApPortMemberApNumber": ruijieApPortMemberApNumber,
       "ruijieApPortMemberAction": ruijieApPortMemberAction,
       "ruijieApPortMemberLacpStatus": ruijieApPortMemberLacpStatus,
       "ruijieApBalcProfName": ruijieApBalcProfName,
       "ruijieApProfTable": ruijieApProfTable,
       "ruijieApProfEntry": ruijieApProfEntry,
       "ruijieApProfIdx": ruijieApProfIdx,
       "ruijieApProfName": ruijieApProfName,
       "ruijieApProfL2SrcMac": ruijieApProfL2SrcMac,
       "ruijieApProfL2DestMac": ruijieApProfL2DestMac,
       "ruijieApProfL2Pro": ruijieApProfL2Pro,
       "ruijieApProfL2Vlan": ruijieApProfL2Vlan,
       "ruijieApProfL2SrcPort": ruijieApProfL2SrcPort,
       "ruijieApProfIpv4SrcIp": ruijieApProfIpv4SrcIp,
       "ruijieApProfIpv4DestIp": ruijieApProfIpv4DestIp,
       "ruijieApProfIpv4Pro": ruijieApProfIpv4Pro,
       "ruijieApProfIpv4L4SrcPort": ruijieApProfIpv4L4SrcPort,
       "ruijieApProfIpv4L4DestPort": ruijieApProfIpv4L4DestPort,
       "ruijieApProfIpv4Vlan": ruijieApProfIpv4Vlan,
       "ruijieApProfIpv4SrcPort": ruijieApProfIpv4SrcPort,
       "ruijieApProfIpv6SrcIp": ruijieApProfIpv6SrcIp,
       "ruijieApProfIpv6DestIp": ruijieApProfIpv6DestIp,
       "ruijieApProfIpv6Pro": ruijieApProfIpv6Pro,
       "ruijieApProfIpv6L4SrcPort": ruijieApProfIpv6L4SrcPort,
       "ruijieApProfIpv6L4DestPort": ruijieApProfIpv6L4DestPort,
       "ruijieApProfIpv6Vlan": ruijieApProfIpv6Vlan,
       "ruijieApProfIpv6SrcPort": ruijieApProfIpv6SrcPort,
       "ruijieApProfMplsTopLabel": ruijieApProfMplsTopLabel,
       "ruijieApProfMpls2ndLabel": ruijieApProfMpls2ndLabel,
       "ruijieApProfMplsSrcIp": ruijieApProfMplsSrcIp,
       "ruijieApProfMplsDestIp": ruijieApProfMplsDestIp,
       "ruijieApProfMplsVlan": ruijieApProfMplsVlan,
       "ruijieApProfMplsSrcPort": ruijieApProfMplsSrcPort,
       "ruijieApMIBConformance": ruijieApMIBConformance,
       "ruijieApMIBCompliances": ruijieApMIBCompliances,
       "ruijieApMIBCompliance": ruijieApMIBCompliance,
       "ruijieApMIBGroups": ruijieApMIBGroups,
       "ruijieApMIBGroup": ruijieApMIBGroup}
)
