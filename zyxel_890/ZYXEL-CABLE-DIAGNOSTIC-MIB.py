# SNMP MIB module (ZYXEL-CABLE-DIAGNOSTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-CABLE-DIAGNOSTIC-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:26:15 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelCableDiagnostic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelCableDiagnosticsStatus_ObjectIdentity = ObjectIdentity
zyxelCableDiagnosticsStatus = _ZyxelCableDiagnosticsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1)
)
_ZyxelCableDiagnosticsPortTable_Object = MibTable
zyxelCableDiagnosticsPortTable = _ZyxelCableDiagnosticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsPortTable.setStatus("current")
_ZyxelCableDiagnosticsPortEntry_Object = MibTableRow
zyxelCableDiagnosticsPortEntry = _ZyxelCableDiagnosticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 1, 1)
)
zyxelCableDiagnosticsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsPortEntry.setStatus("current")


class _ZyCableDiagnosticsPortAction_Type(Integer32):
    """Custom type zyCableDiagnosticsPortAction based on Integer32"""
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
          ("start", 1),
          ("clear", 2))
    )


_ZyCableDiagnosticsPortAction_Type.__name__ = "Integer32"
_ZyCableDiagnosticsPortAction_Object = MibTableColumn
zyCableDiagnosticsPortAction = _ZyCableDiagnosticsPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 1, 1, 1),
    _ZyCableDiagnosticsPortAction_Type()
)
zyCableDiagnosticsPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCableDiagnosticsPortAction.setStatus("current")


class _ZyCableDiagnosticsPortActionStatus_Type(Integer32):
    """Custom type zyCableDiagnosticsPortActionStatus based on Integer32"""
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
        *(("none", 0),
          ("success", 1),
          ("fail", 2),
          ("under-action", 3))
    )


_ZyCableDiagnosticsPortActionStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticsPortActionStatus_Object = MibTableColumn
zyCableDiagnosticsPortActionStatus = _ZyCableDiagnosticsPortActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 1, 1, 2),
    _ZyCableDiagnosticsPortActionStatus_Type()
)
zyCableDiagnosticsPortActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsPortActionStatus.setStatus("current")
_ZyxelCableDiagnosticsResultPortTable_Object = MibTable
zyxelCableDiagnosticsResultPortTable = _ZyxelCableDiagnosticsResultPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsResultPortTable.setStatus("current")
_ZyxelCableDiagnosticsResultPortEntry_Object = MibTableRow
zyxelCableDiagnosticsResultPortEntry = _ZyxelCableDiagnosticsResultPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2, 1)
)
zyxelCableDiagnosticsResultPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-CABLE-DIAGNOSTIC-MIB", "zyCableDiagnosticsResultPortPairIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsResultPortEntry.setStatus("current")


class _ZyCableDiagnosticsResultPortPairIndex_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairIndex based on Integer32"""
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
        *(("pairA", 0),
          ("pairB", 1),
          ("pairC", 2),
          ("pairD", 3))
    )


_ZyCableDiagnosticsResultPortPairIndex_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairIndex_Object = MibTableColumn
zyCableDiagnosticsResultPortPairIndex = _ZyCableDiagnosticsResultPortPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2, 1, 1),
    _ZyCableDiagnosticsResultPortPairIndex_Type()
)
zyCableDiagnosticsResultPortPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairIndex.setStatus("current")


class _ZyCableDiagnosticsResultPortPairStatus_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairStatus based on Integer32"""
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
        *(("ok", 1),
          ("open", 2),
          ("short", 3),
          ("open-short", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticsResultPortPairStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairStatus_Object = MibTableColumn
zyCableDiagnosticsResultPortPairStatus = _ZyCableDiagnosticsResultPortPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2, 1, 2),
    _ZyCableDiagnosticsResultPortPairStatus_Type()
)
zyCableDiagnosticsResultPortPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairStatus.setStatus("current")


class _ZyCableDiagnosticsResultPortPairLength_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupport", -2),
          ("none", -1))
    )


_ZyCableDiagnosticsResultPortPairLength_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairLength_Object = MibTableColumn
zyCableDiagnosticsResultPortPairLength = _ZyCableDiagnosticsResultPortPairLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2, 1, 3),
    _ZyCableDiagnosticsResultPortPairLength_Type()
)
zyCableDiagnosticsResultPortPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairLength.setStatus("current")


class _ZyCableDiagnosticsResultPortPairDistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairDistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupport", -2),
          ("none", -1))
    )


_ZyCableDiagnosticsResultPortPairDistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairDistanceToFault_Object = MibTableColumn
zyCableDiagnosticsResultPortPairDistanceToFault = _ZyCableDiagnosticsResultPortPairDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2, 1, 4),
    _ZyCableDiagnosticsResultPortPairDistanceToFault_Type()
)
zyCableDiagnosticsResultPortPairDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairDistanceToFault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CABLE-DIAGNOSTIC-MIB",
    **{"zyxelCableDiagnostic": zyxelCableDiagnostic,
       "zyxelCableDiagnosticsStatus": zyxelCableDiagnosticsStatus,
       "zyxelCableDiagnosticsPortTable": zyxelCableDiagnosticsPortTable,
       "zyxelCableDiagnosticsPortEntry": zyxelCableDiagnosticsPortEntry,
       "zyCableDiagnosticsPortAction": zyCableDiagnosticsPortAction,
       "zyCableDiagnosticsPortActionStatus": zyCableDiagnosticsPortActionStatus,
       "zyxelCableDiagnosticsResultPortTable": zyxelCableDiagnosticsResultPortTable,
       "zyxelCableDiagnosticsResultPortEntry": zyxelCableDiagnosticsResultPortEntry,
       "zyCableDiagnosticsResultPortPairIndex": zyCableDiagnosticsResultPortPairIndex,
       "zyCableDiagnosticsResultPortPairStatus": zyCableDiagnosticsResultPortPairStatus,
       "zyCableDiagnosticsResultPortPairLength": zyCableDiagnosticsResultPortPairLength,
       "zyCableDiagnosticsResultPortPairDistanceToFault": zyCableDiagnosticsResultPortPairDistanceToFault}
)
