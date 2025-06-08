# SNMP MIB module (FSP3000c-AUTOCDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP3000c-AUTOCDC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(aosCommon,
 fsp3000c) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "aosCommon",
    "fsp3000c")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

fsp3000cAutoCDCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsp3000cAutoCDCMIB.setRevisions(
        ("2016-09-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AutoCdcControlType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("idle", 1),
          ("init", 2),
          ("measure", 3),
          ("validate", 4))
    )



class AutoCdcResultType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("standby", 1),
          ("progress", 2),
          ("initfail", 3),
          ("timeout", 4),
          ("rngerr", 5),
          ("valerr", 6),
          ("success", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Fsp3000cAutoCDCObjects_ObjectIdentity = ObjectIdentity
fsp3000cAutoCDCObjects = _Fsp3000cAutoCDCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1)
)
_AutoCdcStatusTable_Object = MibTable
autoCdcStatusTable = _AutoCdcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    autoCdcStatusTable.setStatus("current")
_AutoCdcStatusEntry_Object = MibTableRow
autoCdcStatusEntry = _AutoCdcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1)
)
autoCdcStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    autoCdcStatusEntry.setStatus("current")
_AutoCdcStatusControlType_Type = AutoCdcControlType
_AutoCdcStatusControlType_Object = MibTableColumn
autoCdcStatusControlType = _AutoCdcStatusControlType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 1),
    _AutoCdcStatusControlType_Type()
)
autoCdcStatusControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoCdcStatusControlType.setStatus("current")
_AutoCdcStatusPercentComplete_Type = Integer32
_AutoCdcStatusPercentComplete_Object = MibTableColumn
autoCdcStatusPercentComplete = _AutoCdcStatusPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 2),
    _AutoCdcStatusPercentComplete_Type()
)
autoCdcStatusPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoCdcStatusPercentComplete.setStatus("current")
_AutoCdcStatusResultType_Type = AutoCdcResultType
_AutoCdcStatusResultType_Object = MibTableColumn
autoCdcStatusResultType = _AutoCdcStatusResultType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 3),
    _AutoCdcStatusResultType_Type()
)
autoCdcStatusResultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoCdcStatusResultType.setStatus("current")
_AutoCdcStatusTodcValueSet_Type = TruthValue
_AutoCdcStatusTodcValueSet_Object = MibTableColumn
autoCdcStatusTodcValueSet = _AutoCdcStatusTodcValueSet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 4),
    _AutoCdcStatusTodcValueSet_Type()
)
autoCdcStatusTodcValueSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoCdcStatusTodcValueSet.setStatus("current")
_AutoCdcStatusTodcValue_Type = Integer32
_AutoCdcStatusTodcValue_Object = MibTableColumn
autoCdcStatusTodcValue = _AutoCdcStatusTodcValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 5),
    _AutoCdcStatusTodcValue_Type()
)
autoCdcStatusTodcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoCdcStatusTodcValue.setStatus("current")
if mibBuilder.loadTexts:
    autoCdcStatusTodcValue.setUnits("ps/nm")
_Fsp3000cAutoCDCConformance_ObjectIdentity = ObjectIdentity
fsp3000cAutoCDCConformance = _Fsp3000cAutoCDCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2)
)
_Fsp3000cAutoCDCCompliances_ObjectIdentity = ObjectIdentity
fsp3000cAutoCDCCompliances = _Fsp3000cAutoCDCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 1)
)
_Fsp3000cAutoCDCGroups_ObjectIdentity = ObjectIdentity
fsp3000cAutoCDCGroups = _Fsp3000cAutoCDCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 2)
)

# Managed Objects groups

fsp3000cAutoCDCObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 2, 1)
)
fsp3000cAutoCDCObjectGroup.setObjects(
      *(("FSP3000c-AUTOCDC-MIB", "autoCdcStatusControlType"),
        ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusPercentComplete"),
        ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusResultType"),
        ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusTodcValueSet"),
        ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusTodcValue"))
)
if mibBuilder.loadTexts:
    fsp3000cAutoCDCObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsp3000cAutoCDCCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 1, 1)
)
fsp3000cAutoCDCCompliance.setObjects(
    ("FSP3000c-AUTOCDC-MIB", "fsp3000cAutoCDCObjectGroup")
)
if mibBuilder.loadTexts:
    fsp3000cAutoCDCCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP3000c-AUTOCDC-MIB",
    **{"AutoCdcControlType": AutoCdcControlType,
       "AutoCdcResultType": AutoCdcResultType,
       "fsp3000cAutoCDCMIB": fsp3000cAutoCDCMIB,
       "fsp3000cAutoCDCObjects": fsp3000cAutoCDCObjects,
       "autoCdcStatusTable": autoCdcStatusTable,
       "autoCdcStatusEntry": autoCdcStatusEntry,
       "autoCdcStatusControlType": autoCdcStatusControlType,
       "autoCdcStatusPercentComplete": autoCdcStatusPercentComplete,
       "autoCdcStatusResultType": autoCdcStatusResultType,
       "autoCdcStatusTodcValueSet": autoCdcStatusTodcValueSet,
       "autoCdcStatusTodcValue": autoCdcStatusTodcValue,
       "fsp3000cAutoCDCConformance": fsp3000cAutoCDCConformance,
       "fsp3000cAutoCDCCompliances": fsp3000cAutoCDCCompliances,
       "fsp3000cAutoCDCCompliance": fsp3000cAutoCDCCompliance,
       "fsp3000cAutoCDCGroups": fsp3000cAutoCDCGroups,
       "fsp3000cAutoCDCObjectGroup": fsp3000cAutoCDCObjectGroup}
)
