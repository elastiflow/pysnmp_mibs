# SNMP MIB module (ZYXEL-IF-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IF-LOOPBACK-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:21 2025
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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIfLoopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIfLoopbackSetup_ObjectIdentity = ObjectIdentity
zyxelIfLoopbackSetup = _ZyxelIfLoopbackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1)
)
_ZyIfLoopbackMaxNumberOfIfs_Type = Integer32
_ZyIfLoopbackMaxNumberOfIfs_Object = MibScalar
zyIfLoopbackMaxNumberOfIfs = _ZyIfLoopbackMaxNumberOfIfs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 1),
    _ZyIfLoopbackMaxNumberOfIfs_Type()
)
zyIfLoopbackMaxNumberOfIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIfLoopbackMaxNumberOfIfs.setStatus("current")
_ZyxelIfLoopbackTable_Object = MibTable
zyxelIfLoopbackTable = _ZyxelIfLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelIfLoopbackTable.setStatus("current")
_ZyxelIfLoopbackEntry_Object = MibTableRow
zyxelIfLoopbackEntry = _ZyxelIfLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1)
)
zyxelIfLoopbackEntry.setIndexNames(
    (0, "ZYXEL-IF-LOOPBACK-MIB", "zyIfLoopbackId"),
)
if mibBuilder.loadTexts:
    zyxelIfLoopbackEntry.setStatus("current")
_ZyIfLoopbackId_Type = Integer32
_ZyIfLoopbackId_Object = MibTableColumn
zyIfLoopbackId = _ZyIfLoopbackId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1, 1),
    _ZyIfLoopbackId_Type()
)
zyIfLoopbackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIfLoopbackId.setStatus("current")
_ZyIfLoopbackName_Type = OctetString
_ZyIfLoopbackName_Object = MibTableColumn
zyIfLoopbackName = _ZyIfLoopbackName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1, 2),
    _ZyIfLoopbackName_Type()
)
zyIfLoopbackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIfLoopbackName.setStatus("current")
_ZyIfLoopbackIpAddress_Type = IpAddress
_ZyIfLoopbackIpAddress_Object = MibTableColumn
zyIfLoopbackIpAddress = _ZyIfLoopbackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1, 3),
    _ZyIfLoopbackIpAddress_Type()
)
zyIfLoopbackIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIfLoopbackIpAddress.setStatus("current")
_ZyIfLoopbackMask_Type = IpAddress
_ZyIfLoopbackMask_Object = MibTableColumn
zyIfLoopbackMask = _ZyIfLoopbackMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1, 4),
    _ZyIfLoopbackMask_Type()
)
zyIfLoopbackMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIfLoopbackMask.setStatus("current")
_ZyIfLoopbackRowStatus_Type = RowStatus
_ZyIfLoopbackRowStatus_Object = MibTableColumn
zyIfLoopbackRowStatus = _ZyIfLoopbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 28, 1, 2, 1, 5),
    _ZyIfLoopbackRowStatus_Type()
)
zyIfLoopbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIfLoopbackRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IF-LOOPBACK-MIB",
    **{"zyxelIfLoopback": zyxelIfLoopback,
       "zyxelIfLoopbackSetup": zyxelIfLoopbackSetup,
       "zyIfLoopbackMaxNumberOfIfs": zyIfLoopbackMaxNumberOfIfs,
       "zyxelIfLoopbackTable": zyxelIfLoopbackTable,
       "zyxelIfLoopbackEntry": zyxelIfLoopbackEntry,
       "zyIfLoopbackId": zyIfLoopbackId,
       "zyIfLoopbackName": zyIfLoopbackName,
       "zyIfLoopbackIpAddress": zyIfLoopbackIpAddress,
       "zyIfLoopbackMask": zyIfLoopbackMask,
       "zyIfLoopbackRowStatus": zyIfLoopbackRowStatus}
)
