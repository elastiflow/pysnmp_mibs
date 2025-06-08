# SNMP MIB module (ZYXEL-CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-CABLE-DIAG-MIB.mib
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
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelCableDiagnosticSetup_ObjectIdentity = ObjectIdentity
zyxelCableDiagnosticSetup = _ZyxelCableDiagnosticSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 1)
)
_ZyxelCableDiagnosticPortTable_Object = MibTable
zyxelCableDiagnosticPortTable = _ZyxelCableDiagnosticPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortTable.setStatus("current")
_ZyxelCableDiagnosticPortEntry_Object = MibTableRow
zyxelCableDiagnosticPortEntry = _ZyxelCableDiagnosticPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 1, 1, 1)
)
zyxelCableDiagnosticPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortEntry.setStatus("current")


class _ZyCableDiagnosticPortAction_Type(Integer32):
    """Custom type zyCableDiagnosticPortAction based on Integer32"""
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


_ZyCableDiagnosticPortAction_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortAction_Object = MibTableColumn
zyCableDiagnosticPortAction = _ZyCableDiagnosticPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 1, 1, 1, 1),
    _ZyCableDiagnosticPortAction_Type()
)
zyCableDiagnosticPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortAction.setStatus("current")
_ZyxelCableDiagnosticStatus_ObjectIdentity = ObjectIdentity
zyxelCableDiagnosticStatus = _ZyxelCableDiagnosticStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2)
)
_ZyxelCableDiagnosticPortStatusTable_Object = MibTable
zyxelCableDiagnosticPortStatusTable = _ZyxelCableDiagnosticPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortStatusTable.setStatus("current")
_ZyxelCableDiagnosticPortStatusEntry_Object = MibTableRow
zyxelCableDiagnosticPortStatusEntry = _ZyxelCableDiagnosticPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 1, 1)
)
zyxelCableDiagnosticPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortStatusEntry.setStatus("current")


class _ZyCableDiagnosticPortStatusActionStatus_Type(Integer32):
    """Custom type zyCableDiagnosticPortStatusActionStatus based on Integer32"""
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
          ("failure", 2),
          ("processing", 3))
    )


_ZyCableDiagnosticPortStatusActionStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortStatusActionStatus_Object = MibTableColumn
zyCableDiagnosticPortStatusActionStatus = _ZyCableDiagnosticPortStatusActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 1, 1, 1),
    _ZyCableDiagnosticPortStatusActionStatus_Type()
)
zyCableDiagnosticPortStatusActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortStatusActionStatus.setStatus("current")
_ZyxelCableDiagnosticPortResultTable_Object = MibTable
zyxelCableDiagnosticPortResultTable = _ZyxelCableDiagnosticPortResultTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortResultTable.setStatus("current")
_ZyxelCableDiagnosticPortResultEntry_Object = MibTableRow
zyxelCableDiagnosticPortResultEntry = _ZyxelCableDiagnosticPortResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1)
)
zyxelCableDiagnosticPortResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticPortResultEntry.setStatus("current")


class _ZyCableDiagnosticPortResultPairAStatus_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairAStatus based on Integer32"""
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
          ("openshort", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticPortResultPairAStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairAStatus_Object = MibTableColumn
zyCableDiagnosticPortResultPairAStatus = _ZyCableDiagnosticPortResultPairAStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 1),
    _ZyCableDiagnosticPortResultPairAStatus_Type()
)
zyCableDiagnosticPortResultPairAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairAStatus.setStatus("current")


class _ZyCableDiagnosticPortResultPairBStatus_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairBStatus based on Integer32"""
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
          ("openshort", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticPortResultPairBStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairBStatus_Object = MibTableColumn
zyCableDiagnosticPortResultPairBStatus = _ZyCableDiagnosticPortResultPairBStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 2),
    _ZyCableDiagnosticPortResultPairBStatus_Type()
)
zyCableDiagnosticPortResultPairBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairBStatus.setStatus("current")


class _ZyCableDiagnosticPortResultPairCStatus_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairCStatus based on Integer32"""
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
          ("openshort", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticPortResultPairCStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairCStatus_Object = MibTableColumn
zyCableDiagnosticPortResultPairCStatus = _ZyCableDiagnosticPortResultPairCStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 3),
    _ZyCableDiagnosticPortResultPairCStatus_Type()
)
zyCableDiagnosticPortResultPairCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairCStatus.setStatus("current")


class _ZyCableDiagnosticPortResultPairDStatus_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairDStatus based on Integer32"""
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
          ("openshort", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticPortResultPairDStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairDStatus_Object = MibTableColumn
zyCableDiagnosticPortResultPairDStatus = _ZyCableDiagnosticPortResultPairDStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 4),
    _ZyCableDiagnosticPortResultPairDStatus_Type()
)
zyCableDiagnosticPortResultPairDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairDStatus.setStatus("current")


class _ZyCableDiagnosticPortResultPairALength_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairALength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairALength_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairALength_Object = MibTableColumn
zyCableDiagnosticPortResultPairALength = _ZyCableDiagnosticPortResultPairALength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 5),
    _ZyCableDiagnosticPortResultPairALength_Type()
)
zyCableDiagnosticPortResultPairALength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairALength.setStatus("current")


class _ZyCableDiagnosticPortResultPairBLength_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairBLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairBLength_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairBLength_Object = MibTableColumn
zyCableDiagnosticPortResultPairBLength = _ZyCableDiagnosticPortResultPairBLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 6),
    _ZyCableDiagnosticPortResultPairBLength_Type()
)
zyCableDiagnosticPortResultPairBLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairBLength.setStatus("current")


class _ZyCableDiagnosticPortResultPairCLength_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairCLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairCLength_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairCLength_Object = MibTableColumn
zyCableDiagnosticPortResultPairCLength = _ZyCableDiagnosticPortResultPairCLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 7),
    _ZyCableDiagnosticPortResultPairCLength_Type()
)
zyCableDiagnosticPortResultPairCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairCLength.setStatus("current")


class _ZyCableDiagnosticPortResultPairDLength_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairDLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairDLength_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairDLength_Object = MibTableColumn
zyCableDiagnosticPortResultPairDLength = _ZyCableDiagnosticPortResultPairDLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 8),
    _ZyCableDiagnosticPortResultPairDLength_Type()
)
zyCableDiagnosticPortResultPairDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairDLength.setStatus("current")


class _ZyCableDiagnosticPortResultPairADistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairADistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairADistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairADistanceToFault_Object = MibTableColumn
zyCableDiagnosticPortResultPairADistanceToFault = _ZyCableDiagnosticPortResultPairADistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 9),
    _ZyCableDiagnosticPortResultPairADistanceToFault_Type()
)
zyCableDiagnosticPortResultPairADistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairADistanceToFault.setStatus("current")


class _ZyCableDiagnosticPortResultPairBDistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairBDistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairBDistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairBDistanceToFault_Object = MibTableColumn
zyCableDiagnosticPortResultPairBDistanceToFault = _ZyCableDiagnosticPortResultPairBDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 10),
    _ZyCableDiagnosticPortResultPairBDistanceToFault_Type()
)
zyCableDiagnosticPortResultPairBDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairBDistanceToFault.setStatus("current")


class _ZyCableDiagnosticPortResultPairCDistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairCDistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairCDistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairCDistanceToFault_Object = MibTableColumn
zyCableDiagnosticPortResultPairCDistanceToFault = _ZyCableDiagnosticPortResultPairCDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 11),
    _ZyCableDiagnosticPortResultPairCDistanceToFault_Type()
)
zyCableDiagnosticPortResultPairCDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairCDistanceToFault.setStatus("current")


class _ZyCableDiagnosticPortResultPairDDistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticPortResultPairDDistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", -2),
          ("notApplicable", -1))
    )


_ZyCableDiagnosticPortResultPairDDistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticPortResultPairDDistanceToFault_Object = MibTableColumn
zyCableDiagnosticPortResultPairDDistanceToFault = _ZyCableDiagnosticPortResultPairDDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 112, 2, 2, 1, 12),
    _ZyCableDiagnosticPortResultPairDDistanceToFault_Type()
)
zyCableDiagnosticPortResultPairDDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticPortResultPairDDistanceToFault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CABLE-DIAG-MIB",
    **{"zyxelCableDiagnostic": zyxelCableDiagnostic,
       "zyxelCableDiagnosticSetup": zyxelCableDiagnosticSetup,
       "zyxelCableDiagnosticPortTable": zyxelCableDiagnosticPortTable,
       "zyxelCableDiagnosticPortEntry": zyxelCableDiagnosticPortEntry,
       "zyCableDiagnosticPortAction": zyCableDiagnosticPortAction,
       "zyxelCableDiagnosticStatus": zyxelCableDiagnosticStatus,
       "zyxelCableDiagnosticPortStatusTable": zyxelCableDiagnosticPortStatusTable,
       "zyxelCableDiagnosticPortStatusEntry": zyxelCableDiagnosticPortStatusEntry,
       "zyCableDiagnosticPortStatusActionStatus": zyCableDiagnosticPortStatusActionStatus,
       "zyxelCableDiagnosticPortResultTable": zyxelCableDiagnosticPortResultTable,
       "zyxelCableDiagnosticPortResultEntry": zyxelCableDiagnosticPortResultEntry,
       "zyCableDiagnosticPortResultPairAStatus": zyCableDiagnosticPortResultPairAStatus,
       "zyCableDiagnosticPortResultPairBStatus": zyCableDiagnosticPortResultPairBStatus,
       "zyCableDiagnosticPortResultPairCStatus": zyCableDiagnosticPortResultPairCStatus,
       "zyCableDiagnosticPortResultPairDStatus": zyCableDiagnosticPortResultPairDStatus,
       "zyCableDiagnosticPortResultPairALength": zyCableDiagnosticPortResultPairALength,
       "zyCableDiagnosticPortResultPairBLength": zyCableDiagnosticPortResultPairBLength,
       "zyCableDiagnosticPortResultPairCLength": zyCableDiagnosticPortResultPairCLength,
       "zyCableDiagnosticPortResultPairDLength": zyCableDiagnosticPortResultPairDLength,
       "zyCableDiagnosticPortResultPairADistanceToFault": zyCableDiagnosticPortResultPairADistanceToFault,
       "zyCableDiagnosticPortResultPairBDistanceToFault": zyCableDiagnosticPortResultPairBDistanceToFault,
       "zyCableDiagnosticPortResultPairCDistanceToFault": zyCableDiagnosticPortResultPairCDistanceToFault,
       "zyCableDiagnosticPortResultPairDDistanceToFault": zyCableDiagnosticPortResultPairDDistanceToFault}
)
