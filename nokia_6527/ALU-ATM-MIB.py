# SNMP MIB module (ALU-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-ATM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(aal5VccEntry,
 atmVclEntry,
 atmVplEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmVclEntry",
    "atmVplEntry")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tAtmIntfStatsEntry,) = mibBuilder.importSymbols(
    "TIMETRA-ATM-MIB",
    "tAtmIntfStatsEntry")


# MODULE-IDENTITY

aluATMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    aluATMMIBModule.setRevisions(
        ("1908-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluAtmMIBConformance_ObjectIdentity = ObjectIdentity
aluAtmMIBConformance = _AluAtmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3)
)
_AluAtmMIBCompliances_ObjectIdentity = ObjectIdentity
aluAtmMIBCompliances = _AluAtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 1)
)
_AluAtmMIBGroups_ObjectIdentity = ObjectIdentity
aluAtmMIBGroups = _AluAtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 2)
)
_AluAtmObjs_ObjectIdentity = ObjectIdentity
aluAtmObjs = _AluAtmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3)
)
_AluAtmExtensionObjs_ObjectIdentity = ObjectIdentity
aluAtmExtensionObjs = _AluAtmExtensionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1)
)
_AeTAtmIntfStatsTable_Object = MibTable
aeTAtmIntfStatsTable = _AeTAtmIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aeTAtmIntfStatsTable.setStatus("current")
_AeTAtmIntfStatsEntry_Object = MibTableRow
aeTAtmIntfStatsEntry = _AeTAtmIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aeTAtmIntfStatsEntry.setStatus("current")
_AeAtmIntfStatsTotalOamCellsRxd_Type = Counter64
_AeAtmIntfStatsTotalOamCellsRxd_Object = MibTableColumn
aeAtmIntfStatsTotalOamCellsRxd = _AeAtmIntfStatsTotalOamCellsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 1, 1, 1),
    _AeAtmIntfStatsTotalOamCellsRxd_Type()
)
aeAtmIntfStatsTotalOamCellsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmIntfStatsTotalOamCellsRxd.setStatus("current")
_AeAtmIntfStatsTotalOamCellsTxd_Type = Counter64
_AeAtmIntfStatsTotalOamCellsTxd_Object = MibTableColumn
aeAtmIntfStatsTotalOamCellsTxd = _AeAtmIntfStatsTotalOamCellsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 1, 1, 2),
    _AeAtmIntfStatsTotalOamCellsTxd_Type()
)
aeAtmIntfStatsTotalOamCellsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmIntfStatsTotalOamCellsTxd.setStatus("current")
_AeTAtmOamVclStatisticsTable_Object = MibTable
aeTAtmOamVclStatisticsTable = _AeTAtmOamVclStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    aeTAtmOamVclStatisticsTable.setStatus("current")
_AeTAtmOamVclStatisticsEntry_Object = MibTableRow
aeTAtmOamVclStatisticsEntry = _AeTAtmOamVclStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aeTAtmOamVclStatisticsEntry.setStatus("current")
_AeAtmVclStatsOamCellsGenerated_Type = Counter32
_AeAtmVclStatsOamCellsGenerated_Object = MibTableColumn
aeAtmVclStatsOamCellsGenerated = _AeAtmVclStatsOamCellsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 2, 1, 1),
    _AeAtmVclStatsOamCellsGenerated_Type()
)
aeAtmVclStatsOamCellsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmVclStatsOamCellsGenerated.setStatus("current")
_AeAtmVclStatsOamCellsGeneratedTxd_Type = Counter32
_AeAtmVclStatsOamCellsGeneratedTxd_Object = MibTableColumn
aeAtmVclStatsOamCellsGeneratedTxd = _AeAtmVclStatsOamCellsGeneratedTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 2, 1, 2),
    _AeAtmVclStatsOamCellsGeneratedTxd_Type()
)
aeAtmVclStatsOamCellsGeneratedTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmVclStatsOamCellsGeneratedTxd.setStatus("current")
_AeTAtmOamVplStatisticsTable_Object = MibTable
aeTAtmOamVplStatisticsTable = _AeTAtmOamVplStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    aeTAtmOamVplStatisticsTable.setStatus("current")
_AeTAtmOamVplStatisticsEntry_Object = MibTableRow
aeTAtmOamVplStatisticsEntry = _AeTAtmOamVplStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aeTAtmOamVplStatisticsEntry.setStatus("current")
_AeAtmVplStatsOamCellsGenerated_Type = Counter32
_AeAtmVplStatsOamCellsGenerated_Object = MibTableColumn
aeAtmVplStatsOamCellsGenerated = _AeAtmVplStatsOamCellsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 3, 1, 1),
    _AeAtmVplStatsOamCellsGenerated_Type()
)
aeAtmVplStatsOamCellsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmVplStatsOamCellsGenerated.setStatus("current")
_AeAtmVplStatsOamCellsGeneratedTxd_Type = Counter32
_AeAtmVplStatsOamCellsGeneratedTxd_Object = MibTableColumn
aeAtmVplStatsOamCellsGeneratedTxd = _AeAtmVplStatsOamCellsGeneratedTxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 3, 1, 2),
    _AeAtmVplStatsOamCellsGeneratedTxd_Type()
)
aeAtmVplStatsOamCellsGeneratedTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAtmVplStatsOamCellsGeneratedTxd.setStatus("current")
_AeAal5VccPppoERelayStatsTable_Object = MibTable
aeAal5VccPppoERelayStatsTable = _AeAal5VccPppoERelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    aeAal5VccPppoERelayStatsTable.setStatus("current")
_AeAal5VccPppoERelayStatsEntry_Object = MibTableRow
aeAal5VccPppoERelayStatsEntry = _AeAal5VccPppoERelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aeAal5VccPppoERelayStatsEntry.setStatus("current")
_AeAal5VccStatsPPPoERelayRxd_Type = Counter64
_AeAal5VccStatsPPPoERelayRxd_Object = MibTableColumn
aeAal5VccStatsPPPoERelayRxd = _AeAal5VccStatsPPPoERelayRxd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4, 1, 1),
    _AeAal5VccStatsPPPoERelayRxd_Type()
)
aeAal5VccStatsPPPoERelayRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAal5VccStatsPPPoERelayRxd.setStatus("current")
_AeAal5VccStatsPPPoERelayMalformed_Type = Counter64
_AeAal5VccStatsPPPoERelayMalformed_Object = MibTableColumn
aeAal5VccStatsPPPoERelayMalformed = _AeAal5VccStatsPPPoERelayMalformed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4, 1, 2),
    _AeAal5VccStatsPPPoERelayMalformed_Type()
)
aeAal5VccStatsPPPoERelayMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAal5VccStatsPPPoERelayMalformed.setStatus("current")
_AeAal5VccStatsPPPoERelayOverflow_Type = Counter64
_AeAal5VccStatsPPPoERelayOverflow_Object = MibTableColumn
aeAal5VccStatsPPPoERelayOverflow = _AeAal5VccStatsPPPoERelayOverflow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4, 1, 3),
    _AeAal5VccStatsPPPoERelayOverflow_Type()
)
aeAal5VccStatsPPPoERelayOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAal5VccStatsPPPoERelayOverflow.setStatus("current")
_AeAal5VccStatsPPPoERelayErrors_Type = Counter64
_AeAal5VccStatsPPPoERelayErrors_Object = MibTableColumn
aeAal5VccStatsPPPoERelayErrors = _AeAal5VccStatsPPPoERelayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 3, 1, 4, 1, 4),
    _AeAal5VccStatsPPPoERelayErrors_Type()
)
aeAal5VccStatsPPPoERelayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAal5VccStatsPPPoERelayErrors.setStatus("current")
_AluAtmNotifyPrefix_ObjectIdentity = ObjectIdentity
aluAtmNotifyPrefix = _AluAtmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 3)
)
tAtmIntfStatsEntry.registerAugmentions(
    ("ALU-ATM-MIB",
     "aeTAtmIntfStatsEntry")
)
aeTAtmIntfStatsEntry.setIndexNames(*tAtmIntfStatsEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ALU-ATM-MIB",
     "aeTAtmOamVclStatisticsEntry")
)
aeTAtmOamVclStatisticsEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("ALU-ATM-MIB",
     "aeTAtmOamVplStatisticsEntry")
)
aeTAtmOamVplStatisticsEntry.setIndexNames(*atmVplEntry.getIndexNames())
aal5VccEntry.registerAugmentions(
    ("ALU-ATM-MIB",
     "aeAal5VccPppoERelayStatsEntry")
)
aeAal5VccPppoERelayStatsEntry.setIndexNames(*aal5VccEntry.getIndexNames())

# Managed Objects groups

aluExtAtmIntfOamStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 2, 1)
)
aluExtAtmIntfOamStatsGroup.setObjects(
      *(("ALU-ATM-MIB", "aeAtmIntfStatsTotalOamCellsRxd"),
        ("ALU-ATM-MIB", "aeAtmIntfStatsTotalOamCellsTxd"))
)
if mibBuilder.loadTexts:
    aluExtAtmIntfOamStatsGroup.setStatus("current")

aluExtAtmVclVplOamStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 2, 2)
)
aluExtAtmVclVplOamStatsGroup.setObjects(
      *(("ALU-ATM-MIB", "aeAtmVclStatsOamCellsGenerated"),
        ("ALU-ATM-MIB", "aeAtmVplStatsOamCellsGenerated"))
)
if mibBuilder.loadTexts:
    aluExtAtmVclVplOamStatsGroup.setStatus("obsolete")

aluExtAtmVclVplOamStatsGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 2, 3)
)
aluExtAtmVclVplOamStatsGroupV3v0.setObjects(
      *(("ALU-ATM-MIB", "aeAtmVclStatsOamCellsGenerated"),
        ("ALU-ATM-MIB", "aeAtmVclStatsOamCellsGeneratedTxd"),
        ("ALU-ATM-MIB", "aeAtmVplStatsOamCellsGenerated"),
        ("ALU-ATM-MIB", "aeAtmVplStatsOamCellsGeneratedTxd"))
)
if mibBuilder.loadTexts:
    aluExtAtmVclVplOamStatsGroupV3v0.setStatus("current")

aeAal5VccPppoERelayStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 2, 4)
)
aeAal5VccPppoERelayStatsGroup.setObjects(
      *(("ALU-ATM-MIB", "aeAal5VccStatsPPPoERelayRxd"),
        ("ALU-ATM-MIB", "aeAal5VccStatsPPPoERelayMalformed"),
        ("ALU-ATM-MIB", "aeAal5VccStatsPPPoERelayOverflow"),
        ("ALU-ATM-MIB", "aeAal5VccStatsPPPoERelayErrors"))
)
if mibBuilder.loadTexts:
    aeAal5VccPppoERelayStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluAtmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 3, 1, 1)
)
aluAtmMIBCompliance.setObjects(
      *(("ALU-ATM-MIB", "aluExtAtmIntfOamStatsGroup"),
        ("ALU-ATM-MIB", "aluExtAtmVclVplOamStatsGroup"))
)
if mibBuilder.loadTexts:
    aluAtmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-ATM-MIB",
    **{"aluATMMIBModule": aluATMMIBModule,
       "aluAtmMIBConformance": aluAtmMIBConformance,
       "aluAtmMIBCompliances": aluAtmMIBCompliances,
       "aluAtmMIBCompliance": aluAtmMIBCompliance,
       "aluAtmMIBGroups": aluAtmMIBGroups,
       "aluExtAtmIntfOamStatsGroup": aluExtAtmIntfOamStatsGroup,
       "aluExtAtmVclVplOamStatsGroup": aluExtAtmVclVplOamStatsGroup,
       "aluExtAtmVclVplOamStatsGroupV3v0": aluExtAtmVclVplOamStatsGroupV3v0,
       "aeAal5VccPppoERelayStatsGroup": aeAal5VccPppoERelayStatsGroup,
       "aluAtmObjs": aluAtmObjs,
       "aluAtmExtensionObjs": aluAtmExtensionObjs,
       "aeTAtmIntfStatsTable": aeTAtmIntfStatsTable,
       "aeTAtmIntfStatsEntry": aeTAtmIntfStatsEntry,
       "aeAtmIntfStatsTotalOamCellsRxd": aeAtmIntfStatsTotalOamCellsRxd,
       "aeAtmIntfStatsTotalOamCellsTxd": aeAtmIntfStatsTotalOamCellsTxd,
       "aeTAtmOamVclStatisticsTable": aeTAtmOamVclStatisticsTable,
       "aeTAtmOamVclStatisticsEntry": aeTAtmOamVclStatisticsEntry,
       "aeAtmVclStatsOamCellsGenerated": aeAtmVclStatsOamCellsGenerated,
       "aeAtmVclStatsOamCellsGeneratedTxd": aeAtmVclStatsOamCellsGeneratedTxd,
       "aeTAtmOamVplStatisticsTable": aeTAtmOamVplStatisticsTable,
       "aeTAtmOamVplStatisticsEntry": aeTAtmOamVplStatisticsEntry,
       "aeAtmVplStatsOamCellsGenerated": aeAtmVplStatsOamCellsGenerated,
       "aeAtmVplStatsOamCellsGeneratedTxd": aeAtmVplStatsOamCellsGeneratedTxd,
       "aeAal5VccPppoERelayStatsTable": aeAal5VccPppoERelayStatsTable,
       "aeAal5VccPppoERelayStatsEntry": aeAal5VccPppoERelayStatsEntry,
       "aeAal5VccStatsPPPoERelayRxd": aeAal5VccStatsPPPoERelayRxd,
       "aeAal5VccStatsPPPoERelayMalformed": aeAal5VccStatsPPPoERelayMalformed,
       "aeAal5VccStatsPPPoERelayOverflow": aeAal5VccStatsPPPoERelayOverflow,
       "aeAal5VccStatsPPPoERelayErrors": aeAal5VccStatsPPPoERelayErrors,
       "aluAtmNotifyPrefix": aluAtmNotifyPrefix}
)
