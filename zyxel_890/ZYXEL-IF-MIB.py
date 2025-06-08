# SNMP MIB module (ZYXEL-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IF-MIB.mib
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

zyxelIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIfSetup_ObjectIdentity = ObjectIdentity
zyxelIfSetup = _ZyxelIfSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1)
)
_ZyIfMaxNumberOfVlanIfs_Type = Integer32
_ZyIfMaxNumberOfVlanIfs_Object = MibScalar
zyIfMaxNumberOfVlanIfs = _ZyIfMaxNumberOfVlanIfs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 1),
    _ZyIfMaxNumberOfVlanIfs_Type()
)
zyIfMaxNumberOfVlanIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIfMaxNumberOfVlanIfs.setStatus("current")
_ZyIfMaxNumberOfLoopbackIfs_Type = Integer32
_ZyIfMaxNumberOfLoopbackIfs_Object = MibScalar
zyIfMaxNumberOfLoopbackIfs = _ZyIfMaxNumberOfLoopbackIfs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 2),
    _ZyIfMaxNumberOfLoopbackIfs_Type()
)
zyIfMaxNumberOfLoopbackIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIfMaxNumberOfLoopbackIfs.setStatus("current")
_ZyxelIfTable_Object = MibTable
zyxelIfTable = _ZyxelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelIfTable.setStatus("current")
_ZyxelIfEntry_Object = MibTableRow
zyxelIfEntry = _ZyxelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1)
)
zyxelIfEntry.setIndexNames(
    (0, "ZYXEL-IF-MIB", "zyIfType"),
    (0, "ZYXEL-IF-MIB", "zyIfId"),
)
if mibBuilder.loadTexts:
    zyxelIfEntry.setStatus("current")


class _ZyIfType_Type(Integer32):
    """Custom type zyIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("loopback", 2))
    )


_ZyIfType_Type.__name__ = "Integer32"
_ZyIfType_Object = MibTableColumn
zyIfType = _ZyIfType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 1),
    _ZyIfType_Type()
)
zyIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIfType.setStatus("current")
_ZyIfId_Type = Integer32
_ZyIfId_Object = MibTableColumn
zyIfId = _ZyIfId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 2),
    _ZyIfId_Type()
)
zyIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIfId.setStatus("current")
_ZyIfRowStatus_Type = RowStatus
_ZyIfRowStatus_Object = MibTableColumn
zyIfRowStatus = _ZyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 3),
    _ZyIfRowStatus_Type()
)
zyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IF-MIB",
    **{"zyxelIf": zyxelIf,
       "zyxelIfSetup": zyxelIfSetup,
       "zyIfMaxNumberOfVlanIfs": zyIfMaxNumberOfVlanIfs,
       "zyIfMaxNumberOfLoopbackIfs": zyIfMaxNumberOfLoopbackIfs,
       "zyxelIfTable": zyxelIfTable,
       "zyxelIfEntry": zyxelIfEntry,
       "zyIfType": zyIfType,
       "zyIfId": zyIfId,
       "zyIfRowStatus": zyIfRowStatus}
)
