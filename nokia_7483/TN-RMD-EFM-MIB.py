# SNMP MIB module (TN-RMD-EFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-RMD-EFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:44 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnRmdIfIndex,) = mibBuilder.importSymbols(
    "TN-RMD-IF-MIB",
    "tnRmdIfIndex")

(tnRmdSystemId,) = mibBuilder.importSymbols(
    "TN-RMD-SYSTEM-MIB",
    "tnRmdSystemId")

(tnRmdMIBModules,
 tnRmdObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnRmdMIBModules",
    "tnRmdObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnRmdEfmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnRmdEfmMibModule.setRevisions(
        ("2012-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnRmdSystemEfmDefect(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("lop", 0)
    )


# MIB Managed Objects in the order of their OIDs

_TnRmdEfmObjects_ObjectIdentity = ObjectIdentity
tnRmdEfmObjects = _TnRmdEfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2)
)
_TnRmdEfmAttributeTotal_Type = Integer32
_TnRmdEfmAttributeTotal_Object = MibScalar
tnRmdEfmAttributeTotal = _TnRmdEfmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 1),
    _TnRmdEfmAttributeTotal_Type()
)
tnRmdEfmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdEfmAttributeTotal.setStatus("current")
_TnRmdSystemEfmTable_Object = MibTable
tnRmdSystemEfmTable = _TnRmdSystemEfmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnRmdSystemEfmTable.setStatus("current")
_TnRmdSystemEfmEntry_Object = MibTableRow
tnRmdSystemEfmEntry = _TnRmdSystemEfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1)
)
tnRmdSystemEfmEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"),
)
if mibBuilder.loadTexts:
    tnRmdSystemEfmEntry.setStatus("current")
_TnRmdSystemEfmEnabled_Type = TruthValue
_TnRmdSystemEfmEnabled_Object = MibTableColumn
tnRmdSystemEfmEnabled = _TnRmdSystemEfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1, 1),
    _TnRmdSystemEfmEnabled_Type()
)
tnRmdSystemEfmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdSystemEfmEnabled.setStatus("current")
_TnRmdSystemEfmDefect_Type = TnRmdSystemEfmDefect
_TnRmdSystemEfmDefect_Object = MibTableColumn
tnRmdSystemEfmDefect = _TnRmdSystemEfmDefect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1, 2),
    _TnRmdSystemEfmDefect_Type()
)
tnRmdSystemEfmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemEfmDefect.setStatus("current")
_TnRmdEfmCountersTable_Object = MibTable
tnRmdEfmCountersTable = _TnRmdEfmCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnRmdEfmCountersTable.setStatus("current")
_TnRmdEfmCountersEntry_Object = MibTableRow
tnRmdEfmCountersEntry = _TnRmdEfmCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1)
)
tnRmdEfmCountersEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"),
)
if mibBuilder.loadTexts:
    tnRmdEfmCountersEntry.setStatus("current")
_TnRmdEfmCountersRxNrNearEndErroredSymbols_Type = Counter64
_TnRmdEfmCountersRxNrNearEndErroredSymbols_Object = MibTableColumn
tnRmdEfmCountersRxNrNearEndErroredSymbols = _TnRmdEfmCountersRxNrNearEndErroredSymbols_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1, 1),
    _TnRmdEfmCountersRxNrNearEndErroredSymbols_Type()
)
tnRmdEfmCountersRxNrNearEndErroredSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdEfmCountersRxNrNearEndErroredSymbols.setStatus("current")
_TnRmdEfmCountersReset_Type = TruthValue
_TnRmdEfmCountersReset_Object = MibTableColumn
tnRmdEfmCountersReset = _TnRmdEfmCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1, 2),
    _TnRmdEfmCountersReset_Type()
)
tnRmdEfmCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdEfmCountersReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-RMD-EFM-MIB",
    **{"TnRmdSystemEfmDefect": TnRmdSystemEfmDefect,
       "tnRmdEfmMibModule": tnRmdEfmMibModule,
       "tnRmdEfmObjects": tnRmdEfmObjects,
       "tnRmdEfmAttributeTotal": tnRmdEfmAttributeTotal,
       "tnRmdSystemEfmTable": tnRmdSystemEfmTable,
       "tnRmdSystemEfmEntry": tnRmdSystemEfmEntry,
       "tnRmdSystemEfmEnabled": tnRmdSystemEfmEnabled,
       "tnRmdSystemEfmDefect": tnRmdSystemEfmDefect,
       "tnRmdEfmCountersTable": tnRmdEfmCountersTable,
       "tnRmdEfmCountersEntry": tnRmdEfmCountersEntry,
       "tnRmdEfmCountersRxNrNearEndErroredSymbols": tnRmdEfmCountersRxNrNearEndErroredSymbols,
       "tnRmdEfmCountersReset": tnRmdEfmCountersReset}
)
