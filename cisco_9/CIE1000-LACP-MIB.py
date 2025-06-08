# SNMP MIB module (CIE1000-LACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-LACP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000Unsigned16,
 CIE1000Unsigned8) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000Unsigned16",
    "CIE1000Unsigned8")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000LacpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35)
)
if mibBuilder.loadTexts:
    cie1000LacpMib.setRevisions(
        ("2014-11-14 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000LacpMibObjects_ObjectIdentity = ObjectIdentity
cie1000LacpMibObjects = _Cie1000LacpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1)
)
_Cie1000LacpConfig_ObjectIdentity = ObjectIdentity
cie1000LacpConfig = _Cie1000LacpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2)
)
_Cie1000LacpConfigPortTable_Object = MibTable
cie1000LacpConfigPortTable = _Cie1000LacpConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000LacpConfigPortTable.setStatus("current")
_Cie1000LacpConfigPortEntry_Object = MibTableRow
cie1000LacpConfigPortEntry = _Cie1000LacpConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1)
)
cie1000LacpConfigPortEntry.setIndexNames(
    (0, "CIE1000-LACP-MIB", "cie1000LacpConfigPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000LacpConfigPortEntry.setStatus("current")
_Cie1000LacpConfigPortInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000LacpConfigPortInterfaceNo_Object = MibTableColumn
cie1000LacpConfigPortInterfaceNo = _Cie1000LacpConfigPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 1),
    _Cie1000LacpConfigPortInterfaceNo_Type()
)
cie1000LacpConfigPortInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortInterfaceNo.setStatus("current")
_Cie1000LacpConfigPortDot3adAggrActorAdminMode_Type = TruthValue
_Cie1000LacpConfigPortDot3adAggrActorAdminMode_Object = MibTableColumn
cie1000LacpConfigPortDot3adAggrActorAdminMode = _Cie1000LacpConfigPortDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 2),
    _Cie1000LacpConfigPortDot3adAggrActorAdminMode_Type()
)
cie1000LacpConfigPortDot3adAggrActorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortDot3adAggrActorAdminMode.setStatus("current")
_Cie1000LacpConfigPortDot3adAggrActorAdminKey_Type = Unsigned32
_Cie1000LacpConfigPortDot3adAggrActorAdminKey_Object = MibTableColumn
cie1000LacpConfigPortDot3adAggrActorAdminKey = _Cie1000LacpConfigPortDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 3),
    _Cie1000LacpConfigPortDot3adAggrActorAdminKey_Type()
)
cie1000LacpConfigPortDot3adAggrActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortDot3adAggrActorAdminKey.setStatus("current")
_Cie1000LacpConfigPortDot3adAggrRole_Type = TruthValue
_Cie1000LacpConfigPortDot3adAggrRole_Object = MibTableColumn
cie1000LacpConfigPortDot3adAggrRole = _Cie1000LacpConfigPortDot3adAggrRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 4),
    _Cie1000LacpConfigPortDot3adAggrRole_Type()
)
cie1000LacpConfigPortDot3adAggrRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortDot3adAggrRole.setStatus("current")
_Cie1000LacpConfigPortDot3adAggrTimeout_Type = TruthValue
_Cie1000LacpConfigPortDot3adAggrTimeout_Object = MibTableColumn
cie1000LacpConfigPortDot3adAggrTimeout = _Cie1000LacpConfigPortDot3adAggrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 5),
    _Cie1000LacpConfigPortDot3adAggrTimeout_Type()
)
cie1000LacpConfigPortDot3adAggrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortDot3adAggrTimeout.setStatus("current")


class _Cie1000LacpConfigPortDot3adAggrPortPriority_Type(Unsigned32):
    """Custom type cie1000LacpConfigPortDot3adAggrPortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cie1000LacpConfigPortDot3adAggrPortPriority_Type.__name__ = "Unsigned32"
_Cie1000LacpConfigPortDot3adAggrPortPriority_Object = MibTableColumn
cie1000LacpConfigPortDot3adAggrPortPriority = _Cie1000LacpConfigPortDot3adAggrPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 1, 1, 6),
    _Cie1000LacpConfigPortDot3adAggrPortPriority_Type()
)
cie1000LacpConfigPortDot3adAggrPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigPortDot3adAggrPortPriority.setStatus("current")
_Cie1000LacpConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000LacpConfigGlobals = _Cie1000LacpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 2)
)


class _Cie1000LacpConfigGlobalsDot3adAggrSystemPriority_Type(Unsigned32):
    """Custom type cie1000LacpConfigGlobalsDot3adAggrSystemPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cie1000LacpConfigGlobalsDot3adAggrSystemPriority_Type.__name__ = "Unsigned32"
_Cie1000LacpConfigGlobalsDot3adAggrSystemPriority_Object = MibScalar
cie1000LacpConfigGlobalsDot3adAggrSystemPriority = _Cie1000LacpConfigGlobalsDot3adAggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 2, 2, 1),
    _Cie1000LacpConfigGlobalsDot3adAggrSystemPriority_Type()
)
cie1000LacpConfigGlobalsDot3adAggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpConfigGlobalsDot3adAggrSystemPriority.setStatus("current")
_Cie1000LacpStatus_ObjectIdentity = ObjectIdentity
cie1000LacpStatus = _Cie1000LacpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3)
)
_Cie1000LacpStatusSystemTable_Object = MibTable
cie1000LacpStatusSystemTable = _Cie1000LacpStatusSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemTable.setStatus("current")
_Cie1000LacpStatusSystemEntry_Object = MibTableRow
cie1000LacpStatusSystemEntry = _Cie1000LacpStatusSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1)
)
cie1000LacpStatusSystemEntry.setIndexNames(
    (0, "CIE1000-LACP-MIB", "cie1000LacpStatusSystemInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemEntry.setStatus("current")
_Cie1000LacpStatusSystemInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000LacpStatusSystemInterfaceNo_Object = MibTableColumn
cie1000LacpStatusSystemInterfaceNo = _Cie1000LacpStatusSystemInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 1),
    _Cie1000LacpStatusSystemInterfaceNo_Type()
)
cie1000LacpStatusSystemInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemInterfaceNo.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrID_Type = CIE1000Unsigned16
_Cie1000LacpStatusSystemDot3adAggrID_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrID = _Cie1000LacpStatusSystemDot3adAggrID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 2),
    _Cie1000LacpStatusSystemDot3adAggrID_Type()
)
cie1000LacpStatusSystemDot3adAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrID.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrPartnerSystemID_Type = MacAddress
_Cie1000LacpStatusSystemDot3adAggrPartnerSystemID_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrPartnerSystemID = _Cie1000LacpStatusSystemDot3adAggrPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 3),
    _Cie1000LacpStatusSystemDot3adAggrPartnerSystemID_Type()
)
cie1000LacpStatusSystemDot3adAggrPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrPartnerSystemID.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrPartnerOperKey_Type = CIE1000Unsigned16
_Cie1000LacpStatusSystemDot3adAggrPartnerOperKey_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrPartnerOperKey = _Cie1000LacpStatusSystemDot3adAggrPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 4),
    _Cie1000LacpStatusSystemDot3adAggrPartnerOperKey_Type()
)
cie1000LacpStatusSystemDot3adAggrPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrPartnerOperKey.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority_Type = CIE1000Unsigned16
_Cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority = _Cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 5),
    _Cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority_Type()
)
cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged_Type = Unsigned32
_Cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged = _Cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 6),
    _Cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged_Type()
)
cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged.setStatus("current")
_Cie1000LacpStatusSystemDot3adAggrLocalPorts_Type = CIE1000PortList
_Cie1000LacpStatusSystemDot3adAggrLocalPorts_Object = MibTableColumn
cie1000LacpStatusSystemDot3adAggrLocalPorts = _Cie1000LacpStatusSystemDot3adAggrLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 1, 1, 7),
    _Cie1000LacpStatusSystemDot3adAggrLocalPorts_Type()
)
cie1000LacpStatusSystemDot3adAggrLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemDot3adAggrLocalPorts.setStatus("current")
_Cie1000LacpStatusPortTable_Object = MibTable
cie1000LacpStatusPortTable = _Cie1000LacpStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000LacpStatusPortTable.setStatus("current")
_Cie1000LacpStatusPortEntry_Object = MibTableRow
cie1000LacpStatusPortEntry = _Cie1000LacpStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1)
)
cie1000LacpStatusPortEntry.setIndexNames(
    (0, "CIE1000-LACP-MIB", "cie1000LacpStatusPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000LacpStatusPortEntry.setStatus("current")
_Cie1000LacpStatusPortInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000LacpStatusPortInterfaceNo_Object = MibTableColumn
cie1000LacpStatusPortInterfaceNo = _Cie1000LacpStatusPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1, 1),
    _Cie1000LacpStatusPortInterfaceNo_Type()
)
cie1000LacpStatusPortInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LacpStatusPortInterfaceNo.setStatus("current")
_Cie1000LacpStatusPortDot3adAggrActorAdminMode_Type = TruthValue
_Cie1000LacpStatusPortDot3adAggrActorAdminMode_Object = MibTableColumn
cie1000LacpStatusPortDot3adAggrActorAdminMode = _Cie1000LacpStatusPortDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1, 2),
    _Cie1000LacpStatusPortDot3adAggrActorAdminMode_Type()
)
cie1000LacpStatusPortDot3adAggrActorAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusPortDot3adAggrActorAdminMode.setStatus("current")
_Cie1000LacpStatusPortDot3adAggrActorAdminKey_Type = CIE1000Unsigned16
_Cie1000LacpStatusPortDot3adAggrActorAdminKey_Object = MibTableColumn
cie1000LacpStatusPortDot3adAggrActorAdminKey = _Cie1000LacpStatusPortDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1, 3),
    _Cie1000LacpStatusPortDot3adAggrActorAdminKey_Type()
)
cie1000LacpStatusPortDot3adAggrActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusPortDot3adAggrActorAdminKey.setStatus("current")
_Cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex_Type = CIE1000Unsigned8
_Cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex_Object = MibTableColumn
cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex = _Cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1, 4),
    _Cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex_Type()
)
cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex.setStatus("current")
_Cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority_Type = CIE1000Unsigned16
_Cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority_Object = MibTableColumn
cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority = _Cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 3, 2, 1, 5),
    _Cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority_Type()
)
cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority.setStatus("current")
_Cie1000LacpControl_ObjectIdentity = ObjectIdentity
cie1000LacpControl = _Cie1000LacpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 4)
)
_Cie1000LacpControlPortStatsClearTable_Object = MibTable
cie1000LacpControlPortStatsClearTable = _Cie1000LacpControlPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000LacpControlPortStatsClearTable.setStatus("current")
_Cie1000LacpControlPortStatsClearEntry_Object = MibTableRow
cie1000LacpControlPortStatsClearEntry = _Cie1000LacpControlPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 4, 1, 1)
)
cie1000LacpControlPortStatsClearEntry.setIndexNames(
    (0, "CIE1000-LACP-MIB", "cie1000LacpControlPortStatsClearInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000LacpControlPortStatsClearEntry.setStatus("current")
_Cie1000LacpControlPortStatsClearInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000LacpControlPortStatsClearInterfaceNo_Object = MibTableColumn
cie1000LacpControlPortStatsClearInterfaceNo = _Cie1000LacpControlPortStatsClearInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 4, 1, 1, 1),
    _Cie1000LacpControlPortStatsClearInterfaceNo_Type()
)
cie1000LacpControlPortStatsClearInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LacpControlPortStatsClearInterfaceNo.setStatus("current")
_Cie1000LacpControlPortStatsClearPortStatisticsClear_Type = TruthValue
_Cie1000LacpControlPortStatsClearPortStatisticsClear_Object = MibTableColumn
cie1000LacpControlPortStatsClearPortStatisticsClear = _Cie1000LacpControlPortStatsClearPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 4, 1, 1, 2),
    _Cie1000LacpControlPortStatsClearPortStatisticsClear_Type()
)
cie1000LacpControlPortStatsClearPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LacpControlPortStatsClearPortStatisticsClear.setStatus("current")
_Cie1000LacpStatistics_ObjectIdentity = ObjectIdentity
cie1000LacpStatistics = _Cie1000LacpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5)
)
_Cie1000LacpStatisticsPortTable_Object = MibTable
cie1000LacpStatisticsPortTable = _Cie1000LacpStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortTable.setStatus("current")
_Cie1000LacpStatisticsPortEntry_Object = MibTableRow
cie1000LacpStatisticsPortEntry = _Cie1000LacpStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1)
)
cie1000LacpStatisticsPortEntry.setIndexNames(
    (0, "CIE1000-LACP-MIB", "cie1000LacpStatisticsPortInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortEntry.setStatus("current")
_Cie1000LacpStatisticsPortInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000LacpStatisticsPortInterfaceNo_Object = MibTableColumn
cie1000LacpStatisticsPortInterfaceNo = _Cie1000LacpStatisticsPortInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1, 1),
    _Cie1000LacpStatisticsPortInterfaceNo_Type()
)
cie1000LacpStatisticsPortInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortInterfaceNo.setStatus("current")
_Cie1000LacpStatisticsPortDot3adAggrRxFrames_Type = Counter64
_Cie1000LacpStatisticsPortDot3adAggrRxFrames_Object = MibTableColumn
cie1000LacpStatisticsPortDot3adAggrRxFrames = _Cie1000LacpStatisticsPortDot3adAggrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1, 2),
    _Cie1000LacpStatisticsPortDot3adAggrRxFrames_Type()
)
cie1000LacpStatisticsPortDot3adAggrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortDot3adAggrRxFrames.setStatus("current")
_Cie1000LacpStatisticsPortDot3adAggrTxFrames_Type = Counter64
_Cie1000LacpStatisticsPortDot3adAggrTxFrames_Object = MibTableColumn
cie1000LacpStatisticsPortDot3adAggrTxFrames = _Cie1000LacpStatisticsPortDot3adAggrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1, 3),
    _Cie1000LacpStatisticsPortDot3adAggrTxFrames_Type()
)
cie1000LacpStatisticsPortDot3adAggrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortDot3adAggrTxFrames.setStatus("current")
_Cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames_Type = Counter64
_Cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames_Object = MibTableColumn
cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames = _Cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1, 4),
    _Cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames_Type()
)
cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames.setStatus("current")
_Cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames_Type = Counter64
_Cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames_Object = MibTableColumn
cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames = _Cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 1, 5, 3, 1, 5),
    _Cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames_Type()
)
cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames.setStatus("current")
_Cie1000LacpMibConformance_ObjectIdentity = ObjectIdentity
cie1000LacpMibConformance = _Cie1000LacpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2)
)
_Cie1000LacpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000LacpMibCompliances = _Cie1000LacpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 1)
)
_Cie1000LacpMibGroups_ObjectIdentity = ObjectIdentity
cie1000LacpMibGroups = _Cie1000LacpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2)
)

# Managed Objects groups

cie1000LacpConfigPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 1)
)
cie1000LacpConfigPortTableInfoGroup.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpConfigPortInterfaceNo"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigPortDot3adAggrActorAdminMode"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigPortDot3adAggrActorAdminKey"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigPortDot3adAggrRole"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigPortDot3adAggrTimeout"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigPortDot3adAggrPortPriority"))
)
if mibBuilder.loadTexts:
    cie1000LacpConfigPortTableInfoGroup.setStatus("current")

cie1000LacpConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 2)
)
cie1000LacpConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-LACP-MIB", "cie1000LacpConfigGlobalsDot3adAggrSystemPriority")
)
if mibBuilder.loadTexts:
    cie1000LacpConfigGlobalsInfoGroup.setStatus("current")

cie1000LacpStatusSystemTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 3)
)
cie1000LacpStatusSystemTableInfoGroup.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpStatusSystemInterfaceNo"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrID"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrPartnerSystemID"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrPartnerOperKey"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemDot3adAggrLocalPorts"))
)
if mibBuilder.loadTexts:
    cie1000LacpStatusSystemTableInfoGroup.setStatus("current")

cie1000LacpStatusPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 4)
)
cie1000LacpStatusPortTableInfoGroup.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpStatusPortInterfaceNo"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusPortDot3adAggrActorAdminMode"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusPortDot3adAggrActorAdminKey"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority"))
)
if mibBuilder.loadTexts:
    cie1000LacpStatusPortTableInfoGroup.setStatus("current")

cie1000LacpControlPortStatsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 5)
)
cie1000LacpControlPortStatsClearTableInfoGroup.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpControlPortStatsClearInterfaceNo"),
        ("CIE1000-LACP-MIB", "cie1000LacpControlPortStatsClearPortStatisticsClear"))
)
if mibBuilder.loadTexts:
    cie1000LacpControlPortStatsClearTableInfoGroup.setStatus("current")

cie1000LacpStatisticsPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 2, 6)
)
cie1000LacpStatisticsPortTableInfoGroup.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortInterfaceNo"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortDot3adAggrRxFrames"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortDot3adAggrTxFrames"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames"))
)
if mibBuilder.loadTexts:
    cie1000LacpStatisticsPortTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000LacpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 35, 2, 1, 1)
)
cie1000LacpMibCompliance.setObjects(
      *(("CIE1000-LACP-MIB", "cie1000LacpConfigPortTableInfoGroup"),
        ("CIE1000-LACP-MIB", "cie1000LacpConfigGlobalsInfoGroup"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusSystemTableInfoGroup"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatusPortTableInfoGroup"),
        ("CIE1000-LACP-MIB", "cie1000LacpControlPortStatsClearTableInfoGroup"),
        ("CIE1000-LACP-MIB", "cie1000LacpStatisticsPortTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000LacpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-LACP-MIB",
    **{"cie1000LacpMib": cie1000LacpMib,
       "cie1000LacpMibObjects": cie1000LacpMibObjects,
       "cie1000LacpConfig": cie1000LacpConfig,
       "cie1000LacpConfigPortTable": cie1000LacpConfigPortTable,
       "cie1000LacpConfigPortEntry": cie1000LacpConfigPortEntry,
       "cie1000LacpConfigPortInterfaceNo": cie1000LacpConfigPortInterfaceNo,
       "cie1000LacpConfigPortDot3adAggrActorAdminMode": cie1000LacpConfigPortDot3adAggrActorAdminMode,
       "cie1000LacpConfigPortDot3adAggrActorAdminKey": cie1000LacpConfigPortDot3adAggrActorAdminKey,
       "cie1000LacpConfigPortDot3adAggrRole": cie1000LacpConfigPortDot3adAggrRole,
       "cie1000LacpConfigPortDot3adAggrTimeout": cie1000LacpConfigPortDot3adAggrTimeout,
       "cie1000LacpConfigPortDot3adAggrPortPriority": cie1000LacpConfigPortDot3adAggrPortPriority,
       "cie1000LacpConfigGlobals": cie1000LacpConfigGlobals,
       "cie1000LacpConfigGlobalsDot3adAggrSystemPriority": cie1000LacpConfigGlobalsDot3adAggrSystemPriority,
       "cie1000LacpStatus": cie1000LacpStatus,
       "cie1000LacpStatusSystemTable": cie1000LacpStatusSystemTable,
       "cie1000LacpStatusSystemEntry": cie1000LacpStatusSystemEntry,
       "cie1000LacpStatusSystemInterfaceNo": cie1000LacpStatusSystemInterfaceNo,
       "cie1000LacpStatusSystemDot3adAggrID": cie1000LacpStatusSystemDot3adAggrID,
       "cie1000LacpStatusSystemDot3adAggrPartnerSystemID": cie1000LacpStatusSystemDot3adAggrPartnerSystemID,
       "cie1000LacpStatusSystemDot3adAggrPartnerOperKey": cie1000LacpStatusSystemDot3adAggrPartnerOperKey,
       "cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority": cie1000LacpStatusSystemDot3adAggrPartnerOperSystemPriority,
       "cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged": cie1000LacpStatusSystemDot3adAggrPartnerStateLastChanged,
       "cie1000LacpStatusSystemDot3adAggrLocalPorts": cie1000LacpStatusSystemDot3adAggrLocalPorts,
       "cie1000LacpStatusPortTable": cie1000LacpStatusPortTable,
       "cie1000LacpStatusPortEntry": cie1000LacpStatusPortEntry,
       "cie1000LacpStatusPortInterfaceNo": cie1000LacpStatusPortInterfaceNo,
       "cie1000LacpStatusPortDot3adAggrActorAdminMode": cie1000LacpStatusPortDot3adAggrActorAdminMode,
       "cie1000LacpStatusPortDot3adAggrActorAdminKey": cie1000LacpStatusPortDot3adAggrActorAdminKey,
       "cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex": cie1000LacpStatusPortDot3adAggrPartnerOperPortIndex,
       "cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority": cie1000LacpStatusPortDot3adAggrPartnerOperPortPriority,
       "cie1000LacpControl": cie1000LacpControl,
       "cie1000LacpControlPortStatsClearTable": cie1000LacpControlPortStatsClearTable,
       "cie1000LacpControlPortStatsClearEntry": cie1000LacpControlPortStatsClearEntry,
       "cie1000LacpControlPortStatsClearInterfaceNo": cie1000LacpControlPortStatsClearInterfaceNo,
       "cie1000LacpControlPortStatsClearPortStatisticsClear": cie1000LacpControlPortStatsClearPortStatisticsClear,
       "cie1000LacpStatistics": cie1000LacpStatistics,
       "cie1000LacpStatisticsPortTable": cie1000LacpStatisticsPortTable,
       "cie1000LacpStatisticsPortEntry": cie1000LacpStatisticsPortEntry,
       "cie1000LacpStatisticsPortInterfaceNo": cie1000LacpStatisticsPortInterfaceNo,
       "cie1000LacpStatisticsPortDot3adAggrRxFrames": cie1000LacpStatisticsPortDot3adAggrRxFrames,
       "cie1000LacpStatisticsPortDot3adAggrTxFrames": cie1000LacpStatisticsPortDot3adAggrTxFrames,
       "cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames": cie1000LacpStatisticsPortDot3adAggrRxIllegalFrames,
       "cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames": cie1000LacpStatisticsPortDot3adAggrRxUnknownFrames,
       "cie1000LacpMibConformance": cie1000LacpMibConformance,
       "cie1000LacpMibCompliances": cie1000LacpMibCompliances,
       "cie1000LacpMibCompliance": cie1000LacpMibCompliance,
       "cie1000LacpMibGroups": cie1000LacpMibGroups,
       "cie1000LacpConfigPortTableInfoGroup": cie1000LacpConfigPortTableInfoGroup,
       "cie1000LacpConfigGlobalsInfoGroup": cie1000LacpConfigGlobalsInfoGroup,
       "cie1000LacpStatusSystemTableInfoGroup": cie1000LacpStatusSystemTableInfoGroup,
       "cie1000LacpStatusPortTableInfoGroup": cie1000LacpStatusPortTableInfoGroup,
       "cie1000LacpControlPortStatsClearTableInfoGroup": cie1000LacpControlPortStatsClearTableInfoGroup,
       "cie1000LacpStatisticsPortTableInfoGroup": cie1000LacpStatisticsPortTableInfoGroup}
)
