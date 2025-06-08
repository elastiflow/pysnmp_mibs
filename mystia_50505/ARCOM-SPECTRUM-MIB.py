# SNMP MIB module (ARCOM-SPECTRUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mystia_50505/ARCOM-SPECTRUM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:36:08 2025
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

(arcomRPD,) = mibBuilder.importSymbols(
    "ARCOM-SMI",
    "arcomRPD")

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

arcomSpectrumMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1)
)
if mibBuilder.loadTexts:
    arcomSpectrumMIB.setRevisions(
        ("2017-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SMStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("busy", 1))
    )



class SpectrumData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1152, 1152),
    )
    fixed_length = 1152



# MIB Managed Objects in the order of their OIDs

_ArcomSpectrumMIBObjects_ObjectIdentity = ObjectIdentity
arcomSpectrumMIBObjects = _ArcomSpectrumMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1)
)
_SmSpectrumRequestInfo_ObjectIdentity = ObjectIdentity
smSpectrumRequestInfo = _SmSpectrumRequestInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 1)
)
_SmSpectrumStatus_Type = SMStatus
_SmSpectrumStatus_Object = MibScalar
smSpectrumStatus = _SmSpectrumStatus_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 1, 1),
    _SmSpectrumStatus_Type()
)
smSpectrumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSpectrumStatus.setStatus("current")
_SmSpectrum4KDataTable_Object = MibTable
smSpectrum4KDataTable = _SmSpectrum4KDataTable_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    smSpectrum4KDataTable.setStatus("current")
_SmSpectrum4KDataEntry_Object = MibTableRow
smSpectrum4KDataEntry = _SmSpectrum4KDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 2, 1)
)
smSpectrum4KDataEntry.setIndexNames(
    (0, "ARCOM-SPECTRUM-MIB", "smSpectrum4KDataIndex"),
)
if mibBuilder.loadTexts:
    smSpectrum4KDataEntry.setStatus("current")


class _SmSpectrum4KDataIndex_Type(Unsigned32):
    """Custom type smSpectrum4KDataIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_SmSpectrum4KDataIndex_Type.__name__ = "Unsigned32"
_SmSpectrum4KDataIndex_Object = MibTableColumn
smSpectrum4KDataIndex = _SmSpectrum4KDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 2, 1, 1),
    _SmSpectrum4KDataIndex_Type()
)
smSpectrum4KDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smSpectrum4KDataIndex.setStatus("current")
_SmSpectrum4KData_Type = SpectrumData
_SmSpectrum4KData_Object = MibTableColumn
smSpectrum4KData = _SmSpectrum4KData_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 2, 1, 2),
    _SmSpectrum4KData_Type()
)
smSpectrum4KData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSpectrum4KData.setStatus("current")
_SmSpectrum8KDataTable_Object = MibTable
smSpectrum8KDataTable = _SmSpectrum8KDataTable_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    smSpectrum8KDataTable.setStatus("current")
_SmSpectrum8KDataEntry_Object = MibTableRow
smSpectrum8KDataEntry = _SmSpectrum8KDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 3, 1)
)
smSpectrum8KDataEntry.setIndexNames(
    (0, "ARCOM-SPECTRUM-MIB", "smSpectrum8KDataIndex"),
)
if mibBuilder.loadTexts:
    smSpectrum8KDataEntry.setStatus("current")


class _SmSpectrum8KDataIndex_Type(Unsigned32):
    """Custom type smSpectrum8KDataIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_SmSpectrum8KDataIndex_Type.__name__ = "Unsigned32"
_SmSpectrum8KDataIndex_Object = MibTableColumn
smSpectrum8KDataIndex = _SmSpectrum8KDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 3, 1, 1),
    _SmSpectrum8KDataIndex_Type()
)
smSpectrum8KDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smSpectrum8KDataIndex.setStatus("current")
_SmSpectrum8KData_Type = SpectrumData
_SmSpectrum8KData_Object = MibTableColumn
smSpectrum8KData = _SmSpectrum8KData_Object(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 1, 3, 1, 2),
    _SmSpectrum8KData_Type()
)
smSpectrum8KData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSpectrum8KData.setStatus("current")
_ArcomSpectrumMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
arcomSpectrumMIBNotificationPrefix = _ArcomSpectrumMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 2)
)
_ArcomSpectrumMIBConformance_ObjectIdentity = ObjectIdentity
arcomSpectrumMIBConformance = _ArcomSpectrumMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 3)
)
_ArcomSpectrumMIBCompliances_ObjectIdentity = ObjectIdentity
arcomSpectrumMIBCompliances = _ArcomSpectrumMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 3, 1)
)
_ArcomSpectrumMIBGroups_ObjectIdentity = ObjectIdentity
arcomSpectrumMIBGroups = _ArcomSpectrumMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 3, 2)
)

# Managed Objects groups

smSpectrumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 3, 2, 1)
)
smSpectrumGroup.setObjects(
      *(("ARCOM-SPECTRUM-MIB", "smSpectrumStatus"),
        ("ARCOM-SPECTRUM-MIB", "smSpectrum4KData"),
        ("ARCOM-SPECTRUM-MIB", "smSpectrum8KData"))
)
if mibBuilder.loadTexts:
    smSpectrumGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 50505, 1, 1, 3, 1, 1)
)
smCompliance.setObjects(
    ("ARCOM-SPECTRUM-MIB", "smSpectrumGroup")
)
if mibBuilder.loadTexts:
    smCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARCOM-SPECTRUM-MIB",
    **{"SMStatus": SMStatus,
       "SpectrumData": SpectrumData,
       "arcomSpectrumMIB": arcomSpectrumMIB,
       "arcomSpectrumMIBObjects": arcomSpectrumMIBObjects,
       "smSpectrumRequestInfo": smSpectrumRequestInfo,
       "smSpectrumStatus": smSpectrumStatus,
       "smSpectrum4KDataTable": smSpectrum4KDataTable,
       "smSpectrum4KDataEntry": smSpectrum4KDataEntry,
       "smSpectrum4KDataIndex": smSpectrum4KDataIndex,
       "smSpectrum4KData": smSpectrum4KData,
       "smSpectrum8KDataTable": smSpectrum8KDataTable,
       "smSpectrum8KDataEntry": smSpectrum8KDataEntry,
       "smSpectrum8KDataIndex": smSpectrum8KDataIndex,
       "smSpectrum8KData": smSpectrum8KData,
       "arcomSpectrumMIBNotificationPrefix": arcomSpectrumMIBNotificationPrefix,
       "arcomSpectrumMIBConformance": arcomSpectrumMIBConformance,
       "arcomSpectrumMIBCompliances": arcomSpectrumMIBCompliances,
       "smCompliance": smCompliance,
       "arcomSpectrumMIBGroups": arcomSpectrumMIBGroups,
       "smSpectrumGroup": smSpectrumGroup}
)
