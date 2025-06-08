# SNMP MIB module (CISCO-VOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VOA-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:40 2025
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

(OpticalIfDirection,) = mibBuilder.importSymbols(
    "CISCO-OPTICAL-MONITOR-MIB",
    "OpticalIfDirection")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoVoaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262)
)
if mibBuilder.loadTexts:
    ciscoVoaMIB.setRevisions(
        ("2002-05-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OpticalPowerInDbm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 250),
        ValueRangeConstraint(-1000, -1000),
    )



class OpticalAttenInDb(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )



# MIB Managed Objects in the order of their OIDs

_CVoaMIBObjects_ObjectIdentity = ObjectIdentity
cVoaMIBObjects = _CVoaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1)
)
_CVoaBaseGroup_ObjectIdentity = ObjectIdentity
cVoaBaseGroup = _CVoaBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1)
)
_CVoaTable_Object = MibTable
cVoaTable = _CVoaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cVoaTable.setStatus("current")
_CVoaEntry_Object = MibTableRow
cVoaEntry = _CVoaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1)
)
cVoaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VOA-MIB", "cVoaDirection"),
)
if mibBuilder.loadTexts:
    cVoaEntry.setStatus("current")
_CVoaDirection_Type = OpticalIfDirection
_CVoaDirection_Object = MibTableColumn
cVoaDirection = _CVoaDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 1),
    _CVoaDirection_Type()
)
cVoaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVoaDirection.setStatus("current")


class _CVoaAttenuationControlMode_Type(Integer32):
    """Custom type cVoaAttenuationControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_CVoaAttenuationControlMode_Type.__name__ = "Integer32"
_CVoaAttenuationControlMode_Object = MibTableColumn
cVoaAttenuationControlMode = _CVoaAttenuationControlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 2),
    _CVoaAttenuationControlMode_Type()
)
cVoaAttenuationControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVoaAttenuationControlMode.setStatus("current")
_CVoaAttenuation_Type = OpticalAttenInDb
_CVoaAttenuation_Object = MibTableColumn
cVoaAttenuation = _CVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 3),
    _CVoaAttenuation_Type()
)
cVoaAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVoaAttenuation.setStatus("current")
_CVoaAttenuationLastChange_Type = TimeStamp
_CVoaAttenuationLastChange_Object = MibTableColumn
cVoaAttenuationLastChange = _CVoaAttenuationLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 4),
    _CVoaAttenuationLastChange_Type()
)
cVoaAttenuationLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVoaAttenuationLastChange.setStatus("current")
_CVoaDesiredPower_Type = OpticalPowerInDbm
_CVoaDesiredPower_Object = MibTableColumn
cVoaDesiredPower = _CVoaDesiredPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 5),
    _CVoaDesiredPower_Type()
)
cVoaDesiredPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVoaDesiredPower.setStatus("current")
_CVoaMIBConformance_ObjectIdentity = ObjectIdentity
cVoaMIBConformance = _CVoaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 3)
)
_CVoaMIBCompliances_ObjectIdentity = ObjectIdentity
cVoaMIBCompliances = _CVoaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1)
)
_CVoaMIBGroups_ObjectIdentity = ObjectIdentity
cVoaMIBGroups = _CVoaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2)
)

# Managed Objects groups

cVoaMIBBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2, 1)
)
cVoaMIBBaseGroup.setObjects(
      *(("CISCO-VOA-MIB", "cVoaAttenuationControlMode"),
        ("CISCO-VOA-MIB", "cVoaAttenuation"),
        ("CISCO-VOA-MIB", "cVoaAttenuationLastChange"),
        ("CISCO-VOA-MIB", "cVoaDesiredPower"))
)
if mibBuilder.loadTexts:
    cVoaMIBBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cVoaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1, 1)
)
cVoaMIBCompliance.setObjects(
    ("CISCO-VOA-MIB", "cVoaMIBBaseGroup")
)
if mibBuilder.loadTexts:
    cVoaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOA-MIB",
    **{"OpticalPowerInDbm": OpticalPowerInDbm,
       "OpticalAttenInDb": OpticalAttenInDb,
       "ciscoVoaMIB": ciscoVoaMIB,
       "cVoaMIBObjects": cVoaMIBObjects,
       "cVoaBaseGroup": cVoaBaseGroup,
       "cVoaTable": cVoaTable,
       "cVoaEntry": cVoaEntry,
       "cVoaDirection": cVoaDirection,
       "cVoaAttenuationControlMode": cVoaAttenuationControlMode,
       "cVoaAttenuation": cVoaAttenuation,
       "cVoaAttenuationLastChange": cVoaAttenuationLastChange,
       "cVoaDesiredPower": cVoaDesiredPower,
       "cVoaMIBConformance": cVoaMIBConformance,
       "cVoaMIBCompliances": cVoaMIBCompliances,
       "cVoaMIBCompliance": cVoaMIBCompliance,
       "cVoaMIBGroups": cVoaMIBGroups,
       "cVoaMIBBaseGroup": cVoaMIBBaseGroup}
)
