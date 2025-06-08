# SNMP MIB module (ARISTA-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-VXLAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aristaVxlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28)
)
if mibBuilder.loadTexts:
    aristaVxlanMIB.setRevisions(
        ("2022-09-15 00:00",
         "2020-06-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaVxlanMibNotifications_ObjectIdentity = ObjectIdentity
aristaVxlanMibNotifications = _AristaVxlanMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 0)
)
_AristaVxlanMibObjects_ObjectIdentity = ObjectIdentity
aristaVxlanMibObjects = _AristaVxlanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1)
)
_AristaVxlanVtepCountersTable_Object = MibTable
aristaVxlanVtepCountersTable = _AristaVxlanVtepCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1)
)
if mibBuilder.loadTexts:
    aristaVxlanVtepCountersTable.setStatus("current")
_AristaVxlanVtepCountersEntry_Object = MibTableRow
aristaVxlanVtepCountersEntry = _AristaVxlanVtepCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1)
)
aristaVxlanVtepCountersEntry.setIndexNames(
    (0, "ARISTA-VXLAN-MIB", "aristaVxlanVtepAddressType"),
    (0, "ARISTA-VXLAN-MIB", "aristaVxlanVtepAddress"),
)
if mibBuilder.loadTexts:
    aristaVxlanVtepCountersEntry.setStatus("current")
_AristaVxlanVtepAddressType_Type = InetAddressType
_AristaVxlanVtepAddressType_Object = MibTableColumn
aristaVxlanVtepAddressType = _AristaVxlanVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 1),
    _AristaVxlanVtepAddressType_Type()
)
aristaVxlanVtepAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaVxlanVtepAddressType.setStatus("current")


class _AristaVxlanVtepAddress_Type(InetAddress):
    """Custom type aristaVxlanVtepAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AristaVxlanVtepAddress_Type.__name__ = "InetAddress"
_AristaVxlanVtepAddress_Object = MibTableColumn
aristaVxlanVtepAddress = _AristaVxlanVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 2),
    _AristaVxlanVtepAddress_Type()
)
aristaVxlanVtepAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaVxlanVtepAddress.setStatus("current")
_AristaVxlanVtepDecapBytes_Type = Counter64
_AristaVxlanVtepDecapBytes_Object = MibTableColumn
aristaVxlanVtepDecapBytes = _AristaVxlanVtepDecapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 3),
    _AristaVxlanVtepDecapBytes_Type()
)
aristaVxlanVtepDecapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapBytes.setStatus("current")
_AristaVxlanVtepDecapPkts_Type = Counter64
_AristaVxlanVtepDecapPkts_Object = MibTableColumn
aristaVxlanVtepDecapPkts = _AristaVxlanVtepDecapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 4),
    _AristaVxlanVtepDecapPkts_Type()
)
aristaVxlanVtepDecapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapPkts.setStatus("current")
_AristaVxlanVtepDecapKnownUcastBytes_Type = Counter64
_AristaVxlanVtepDecapKnownUcastBytes_Object = MibTableColumn
aristaVxlanVtepDecapKnownUcastBytes = _AristaVxlanVtepDecapKnownUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 5),
    _AristaVxlanVtepDecapKnownUcastBytes_Type()
)
aristaVxlanVtepDecapKnownUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapKnownUcastBytes.setStatus("current")
_AristaVxlanVtepDecapKnownUcastPkts_Type = Counter64
_AristaVxlanVtepDecapKnownUcastPkts_Object = MibTableColumn
aristaVxlanVtepDecapKnownUcastPkts = _AristaVxlanVtepDecapKnownUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 6),
    _AristaVxlanVtepDecapKnownUcastPkts_Type()
)
aristaVxlanVtepDecapKnownUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapKnownUcastPkts.setStatus("current")
_AristaVxlanVtepDecapBUMBytes_Type = Counter64
_AristaVxlanVtepDecapBUMBytes_Object = MibTableColumn
aristaVxlanVtepDecapBUMBytes = _AristaVxlanVtepDecapBUMBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 7),
    _AristaVxlanVtepDecapBUMBytes_Type()
)
aristaVxlanVtepDecapBUMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapBUMBytes.setStatus("current")
_AristaVxlanVtepDecapBUMPkts_Type = Counter64
_AristaVxlanVtepDecapBUMPkts_Object = MibTableColumn
aristaVxlanVtepDecapBUMPkts = _AristaVxlanVtepDecapBUMPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 8),
    _AristaVxlanVtepDecapBUMPkts_Type()
)
aristaVxlanVtepDecapBUMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapBUMPkts.setStatus("current")
_AristaVxlanVtepDecapDropExcptBytes_Type = Counter64
_AristaVxlanVtepDecapDropExcptBytes_Object = MibTableColumn
aristaVxlanVtepDecapDropExcptBytes = _AristaVxlanVtepDecapDropExcptBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 9),
    _AristaVxlanVtepDecapDropExcptBytes_Type()
)
aristaVxlanVtepDecapDropExcptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapDropExcptBytes.setStatus("current")
_AristaVxlanVtepDecapDropExcptPkts_Type = Counter64
_AristaVxlanVtepDecapDropExcptPkts_Object = MibTableColumn
aristaVxlanVtepDecapDropExcptPkts = _AristaVxlanVtepDecapDropExcptPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 10),
    _AristaVxlanVtepDecapDropExcptPkts_Type()
)
aristaVxlanVtepDecapDropExcptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepDecapDropExcptPkts.setStatus("current")
_AristaVxlanVtepEncapBytes_Type = Counter64
_AristaVxlanVtepEncapBytes_Object = MibTableColumn
aristaVxlanVtepEncapBytes = _AristaVxlanVtepEncapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 11),
    _AristaVxlanVtepEncapBytes_Type()
)
aristaVxlanVtepEncapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepEncapBytes.setStatus("current")
_AristaVxlanVtepEncapPkts_Type = Counter64
_AristaVxlanVtepEncapPkts_Object = MibTableColumn
aristaVxlanVtepEncapPkts = _AristaVxlanVtepEncapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 12),
    _AristaVxlanVtepEncapPkts_Type()
)
aristaVxlanVtepEncapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepEncapPkts.setStatus("current")
_AristaVxlanVtepEncapBUMPkts_Type = Counter64
_AristaVxlanVtepEncapBUMPkts_Object = MibTableColumn
aristaVxlanVtepEncapBUMPkts = _AristaVxlanVtepEncapBUMPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 13),
    _AristaVxlanVtepEncapBUMPkts_Type()
)
aristaVxlanVtepEncapBUMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepEncapBUMPkts.setStatus("current")
_AristaVxlanVtepEncapDropExcptPkts_Type = Counter64
_AristaVxlanVtepEncapDropExcptPkts_Object = MibTableColumn
aristaVxlanVtepEncapDropExcptPkts = _AristaVxlanVtepEncapDropExcptPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 1, 1, 14),
    _AristaVxlanVtepEncapDropExcptPkts_Type()
)
aristaVxlanVtepEncapDropExcptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtepEncapDropExcptPkts.setStatus("current")
_AristaVxlanVniCountersTable_Object = MibTable
aristaVxlanVniCountersTable = _AristaVxlanVniCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2)
)
if mibBuilder.loadTexts:
    aristaVxlanVniCountersTable.setStatus("current")
_AristaVxlanVniCountersEntry_Object = MibTableRow
aristaVxlanVniCountersEntry = _AristaVxlanVniCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1)
)
aristaVxlanVniCountersEntry.setIndexNames(
    (0, "ARISTA-VXLAN-MIB", "aristaVxlanVni"),
)
if mibBuilder.loadTexts:
    aristaVxlanVniCountersEntry.setStatus("current")
_AristaVxlanVni_Type = Unsigned32
_AristaVxlanVni_Object = MibTableColumn
aristaVxlanVni = _AristaVxlanVni_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 1),
    _AristaVxlanVni_Type()
)
aristaVxlanVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaVxlanVni.setStatus("current")
_AristaVxlanVniDecapBytes_Type = Counter64
_AristaVxlanVniDecapBytes_Object = MibTableColumn
aristaVxlanVniDecapBytes = _AristaVxlanVniDecapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 2),
    _AristaVxlanVniDecapBytes_Type()
)
aristaVxlanVniDecapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapBytes.setStatus("current")
_AristaVxlanVniDecapPkts_Type = Counter64
_AristaVxlanVniDecapPkts_Object = MibTableColumn
aristaVxlanVniDecapPkts = _AristaVxlanVniDecapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 3),
    _AristaVxlanVniDecapPkts_Type()
)
aristaVxlanVniDecapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapPkts.setStatus("current")
_AristaVxlanVniDecapKnownUcastBytes_Type = Counter64
_AristaVxlanVniDecapKnownUcastBytes_Object = MibTableColumn
aristaVxlanVniDecapKnownUcastBytes = _AristaVxlanVniDecapKnownUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 4),
    _AristaVxlanVniDecapKnownUcastBytes_Type()
)
aristaVxlanVniDecapKnownUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapKnownUcastBytes.setStatus("current")
_AristaVxlanVniDecapKnownUcastPkts_Type = Counter64
_AristaVxlanVniDecapKnownUcastPkts_Object = MibTableColumn
aristaVxlanVniDecapKnownUcastPkts = _AristaVxlanVniDecapKnownUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 5),
    _AristaVxlanVniDecapKnownUcastPkts_Type()
)
aristaVxlanVniDecapKnownUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapKnownUcastPkts.setStatus("current")
_AristaVxlanVniDecapBUMBytes_Type = Counter64
_AristaVxlanVniDecapBUMBytes_Object = MibTableColumn
aristaVxlanVniDecapBUMBytes = _AristaVxlanVniDecapBUMBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 6),
    _AristaVxlanVniDecapBUMBytes_Type()
)
aristaVxlanVniDecapBUMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapBUMBytes.setStatus("current")
_AristaVxlanVniDecapBUMPkts_Type = Counter64
_AristaVxlanVniDecapBUMPkts_Object = MibTableColumn
aristaVxlanVniDecapBUMPkts = _AristaVxlanVniDecapBUMPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 7),
    _AristaVxlanVniDecapBUMPkts_Type()
)
aristaVxlanVniDecapBUMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapBUMPkts.setStatus("current")
_AristaVxlanVniDecapDropExcptBytes_Type = Counter64
_AristaVxlanVniDecapDropExcptBytes_Object = MibTableColumn
aristaVxlanVniDecapDropExcptBytes = _AristaVxlanVniDecapDropExcptBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 8),
    _AristaVxlanVniDecapDropExcptBytes_Type()
)
aristaVxlanVniDecapDropExcptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapDropExcptBytes.setStatus("current")
_AristaVxlanVniDecapDropExcptPkts_Type = Counter64
_AristaVxlanVniDecapDropExcptPkts_Object = MibTableColumn
aristaVxlanVniDecapDropExcptPkts = _AristaVxlanVniDecapDropExcptPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 9),
    _AristaVxlanVniDecapDropExcptPkts_Type()
)
aristaVxlanVniDecapDropExcptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniDecapDropExcptPkts.setStatus("current")
_AristaVxlanVniEncapBytes_Type = Counter64
_AristaVxlanVniEncapBytes_Object = MibTableColumn
aristaVxlanVniEncapBytes = _AristaVxlanVniEncapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 10),
    _AristaVxlanVniEncapBytes_Type()
)
aristaVxlanVniEncapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniEncapBytes.setStatus("current")
_AristaVxlanVniEncapPkts_Type = Counter64
_AristaVxlanVniEncapPkts_Object = MibTableColumn
aristaVxlanVniEncapPkts = _AristaVxlanVniEncapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 11),
    _AristaVxlanVniEncapPkts_Type()
)
aristaVxlanVniEncapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniEncapPkts.setStatus("current")
_AristaVxlanVniEncapBUMBytes_Type = Counter64
_AristaVxlanVniEncapBUMBytes_Object = MibTableColumn
aristaVxlanVniEncapBUMBytes = _AristaVxlanVniEncapBUMBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 12),
    _AristaVxlanVniEncapBUMBytes_Type()
)
aristaVxlanVniEncapBUMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniEncapBUMBytes.setStatus("current")
_AristaVxlanVniEncapBUMPkts_Type = Counter64
_AristaVxlanVniEncapBUMPkts_Object = MibTableColumn
aristaVxlanVniEncapBUMPkts = _AristaVxlanVniEncapBUMPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 13),
    _AristaVxlanVniEncapBUMPkts_Type()
)
aristaVxlanVniEncapBUMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniEncapBUMPkts.setStatus("current")
_AristaVxlanVniEncapDropPkts_Type = Counter64
_AristaVxlanVniEncapDropPkts_Object = MibTableColumn
aristaVxlanVniEncapDropPkts = _AristaVxlanVniEncapDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 2, 1, 14),
    _AristaVxlanVniEncapDropPkts_Type()
)
aristaVxlanVniEncapDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVniEncapDropPkts.setStatus("current")
_AristaVxlanVtiVniCountersTable_Object = MibTable
aristaVxlanVtiVniCountersTable = _AristaVxlanVtiVniCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3)
)
if mibBuilder.loadTexts:
    aristaVxlanVtiVniCountersTable.setStatus("current")
_AristaVxlanVtiVniCountersEntry_Object = MibTableRow
aristaVxlanVtiVniCountersEntry = _AristaVxlanVtiVniCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1)
)
aristaVxlanVtiVniCountersEntry.setIndexNames(
    (0, "ARISTA-VXLAN-MIB", "aristaVxlanVtiIndex"),
    (0, "ARISTA-VXLAN-MIB", "aristaVxlanVni"),
)
if mibBuilder.loadTexts:
    aristaVxlanVtiVniCountersEntry.setStatus("current")
_AristaVxlanVtiIndex_Type = InterfaceIndex
_AristaVxlanVtiIndex_Object = MibTableColumn
aristaVxlanVtiIndex = _AristaVxlanVtiIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1, 1),
    _AristaVxlanVtiIndex_Type()
)
aristaVxlanVtiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaVxlanVtiIndex.setStatus("current")
_AristaVxlanVtiVniDecapBytes_Type = Counter64
_AristaVxlanVtiVniDecapBytes_Object = MibTableColumn
aristaVxlanVtiVniDecapBytes = _AristaVxlanVtiVniDecapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1, 2),
    _AristaVxlanVtiVniDecapBytes_Type()
)
aristaVxlanVtiVniDecapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtiVniDecapBytes.setStatus("current")
_AristaVxlanVtiVniDecapPkts_Type = Counter64
_AristaVxlanVtiVniDecapPkts_Object = MibTableColumn
aristaVxlanVtiVniDecapPkts = _AristaVxlanVtiVniDecapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1, 3),
    _AristaVxlanVtiVniDecapPkts_Type()
)
aristaVxlanVtiVniDecapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtiVniDecapPkts.setStatus("current")
_AristaVxlanVtiVniEncapBytes_Type = Counter64
_AristaVxlanVtiVniEncapBytes_Object = MibTableColumn
aristaVxlanVtiVniEncapBytes = _AristaVxlanVtiVniEncapBytes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1, 4),
    _AristaVxlanVtiVniEncapBytes_Type()
)
aristaVxlanVtiVniEncapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtiVniEncapBytes.setStatus("current")
_AristaVxlanVtiVniEncapPkts_Type = Counter64
_AristaVxlanVtiVniEncapPkts_Object = MibTableColumn
aristaVxlanVtiVniEncapPkts = _AristaVxlanVtiVniEncapPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 1, 3, 1, 5),
    _AristaVxlanVtiVniEncapPkts_Type()
)
aristaVxlanVtiVniEncapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVxlanVtiVniEncapPkts.setStatus("current")
_AristaVxlanMibConformance_ObjectIdentity = ObjectIdentity
aristaVxlanMibConformance = _AristaVxlanMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 2)
)
_AristaVxlanMibCompliances_ObjectIdentity = ObjectIdentity
aristaVxlanMibCompliances = _AristaVxlanMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 2, 1)
)
_AristaVxlanMibGroups_ObjectIdentity = ObjectIdentity
aristaVxlanMibGroups = _AristaVxlanMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 2, 2)
)

# Managed Objects groups

aristaVxlanMibCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 2, 2, 1)
)
aristaVxlanMibCountersGroup.setObjects(
      *(("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapKnownUcastBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapKnownUcastPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapBUMBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapBUMPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapDropExcptBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepDecapDropExcptPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepEncapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepEncapPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepEncapBUMPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtepEncapDropExcptPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapKnownUcastBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapKnownUcastPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapBUMBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapBUMPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapDropExcptBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniDecapDropExcptPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniEncapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniEncapPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniEncapBUMBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniEncapBUMPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVniEncapDropPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtiVniDecapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtiVniDecapPkts"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtiVniEncapBytes"),
        ("ARISTA-VXLAN-MIB", "aristaVxlanVtiVniEncapPkts"))
)
if mibBuilder.loadTexts:
    aristaVxlanMibCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaVxlanMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 28, 2, 1, 1)
)
aristaVxlanMibCompliance.setObjects(
    ("ARISTA-VXLAN-MIB", "aristaVxlanMibCountersGroup")
)
if mibBuilder.loadTexts:
    aristaVxlanMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-VXLAN-MIB",
    **{"aristaVxlanMIB": aristaVxlanMIB,
       "aristaVxlanMibNotifications": aristaVxlanMibNotifications,
       "aristaVxlanMibObjects": aristaVxlanMibObjects,
       "aristaVxlanVtepCountersTable": aristaVxlanVtepCountersTable,
       "aristaVxlanVtepCountersEntry": aristaVxlanVtepCountersEntry,
       "aristaVxlanVtepAddressType": aristaVxlanVtepAddressType,
       "aristaVxlanVtepAddress": aristaVxlanVtepAddress,
       "aristaVxlanVtepDecapBytes": aristaVxlanVtepDecapBytes,
       "aristaVxlanVtepDecapPkts": aristaVxlanVtepDecapPkts,
       "aristaVxlanVtepDecapKnownUcastBytes": aristaVxlanVtepDecapKnownUcastBytes,
       "aristaVxlanVtepDecapKnownUcastPkts": aristaVxlanVtepDecapKnownUcastPkts,
       "aristaVxlanVtepDecapBUMBytes": aristaVxlanVtepDecapBUMBytes,
       "aristaVxlanVtepDecapBUMPkts": aristaVxlanVtepDecapBUMPkts,
       "aristaVxlanVtepDecapDropExcptBytes": aristaVxlanVtepDecapDropExcptBytes,
       "aristaVxlanVtepDecapDropExcptPkts": aristaVxlanVtepDecapDropExcptPkts,
       "aristaVxlanVtepEncapBytes": aristaVxlanVtepEncapBytes,
       "aristaVxlanVtepEncapPkts": aristaVxlanVtepEncapPkts,
       "aristaVxlanVtepEncapBUMPkts": aristaVxlanVtepEncapBUMPkts,
       "aristaVxlanVtepEncapDropExcptPkts": aristaVxlanVtepEncapDropExcptPkts,
       "aristaVxlanVniCountersTable": aristaVxlanVniCountersTable,
       "aristaVxlanVniCountersEntry": aristaVxlanVniCountersEntry,
       "aristaVxlanVni": aristaVxlanVni,
       "aristaVxlanVniDecapBytes": aristaVxlanVniDecapBytes,
       "aristaVxlanVniDecapPkts": aristaVxlanVniDecapPkts,
       "aristaVxlanVniDecapKnownUcastBytes": aristaVxlanVniDecapKnownUcastBytes,
       "aristaVxlanVniDecapKnownUcastPkts": aristaVxlanVniDecapKnownUcastPkts,
       "aristaVxlanVniDecapBUMBytes": aristaVxlanVniDecapBUMBytes,
       "aristaVxlanVniDecapBUMPkts": aristaVxlanVniDecapBUMPkts,
       "aristaVxlanVniDecapDropExcptBytes": aristaVxlanVniDecapDropExcptBytes,
       "aristaVxlanVniDecapDropExcptPkts": aristaVxlanVniDecapDropExcptPkts,
       "aristaVxlanVniEncapBytes": aristaVxlanVniEncapBytes,
       "aristaVxlanVniEncapPkts": aristaVxlanVniEncapPkts,
       "aristaVxlanVniEncapBUMBytes": aristaVxlanVniEncapBUMBytes,
       "aristaVxlanVniEncapBUMPkts": aristaVxlanVniEncapBUMPkts,
       "aristaVxlanVniEncapDropPkts": aristaVxlanVniEncapDropPkts,
       "aristaVxlanVtiVniCountersTable": aristaVxlanVtiVniCountersTable,
       "aristaVxlanVtiVniCountersEntry": aristaVxlanVtiVniCountersEntry,
       "aristaVxlanVtiIndex": aristaVxlanVtiIndex,
       "aristaVxlanVtiVniDecapBytes": aristaVxlanVtiVniDecapBytes,
       "aristaVxlanVtiVniDecapPkts": aristaVxlanVtiVniDecapPkts,
       "aristaVxlanVtiVniEncapBytes": aristaVxlanVtiVniEncapBytes,
       "aristaVxlanVtiVniEncapPkts": aristaVxlanVtiVniEncapPkts,
       "aristaVxlanMibConformance": aristaVxlanMibConformance,
       "aristaVxlanMibCompliances": aristaVxlanMibCompliances,
       "aristaVxlanMibCompliance": aristaVxlanMibCompliance,
       "aristaVxlanMibGroups": aristaVxlanMibGroups,
       "aristaVxlanMibCountersGroup": aristaVxlanMibCountersGroup}
)
