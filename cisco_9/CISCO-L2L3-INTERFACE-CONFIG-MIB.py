# SNMP MIB module (CISCO-L2L3-INTERFACE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-L2L3-INTERFACE-CONFIG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:33 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoL2L3IfConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151)
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigMIB.setRevisions(
        ("2000-05-10 19:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CL2L3InterfaceMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routed", 1),
          ("switchport", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoL2L3IfConfigMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBObjects = _CiscoL2L3IfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1)
)
_CL2L3IfConfig_ObjectIdentity = ObjectIdentity
cL2L3IfConfig = _CL2L3IfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1)
)
_CL2L3IfTable_Object = MibTable
cL2L3IfTable = _CL2L3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cL2L3IfTable.setStatus("current")
_CL2L3IfEntry_Object = MibTableRow
cL2L3IfEntry = _CL2L3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1)
)
cL2L3IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cL2L3IfEntry.setStatus("current")
_CL2L3IfModeAdmin_Type = CL2L3InterfaceMode
_CL2L3IfModeAdmin_Object = MibTableColumn
cL2L3IfModeAdmin = _CL2L3IfModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1),
    _CL2L3IfModeAdmin_Type()
)
cL2L3IfModeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cL2L3IfModeAdmin.setStatus("current")
_CL2L3IfModeOper_Type = CL2L3InterfaceMode
_CL2L3IfModeOper_Object = MibTableColumn
cL2L3IfModeOper = _CL2L3IfModeOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2),
    _CL2L3IfModeOper_Type()
)
cL2L3IfModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cL2L3IfModeOper.setStatus("current")
_CiscoL2L3IfConfigMIBConformance_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBConformance = _CiscoL2L3IfConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3)
)
_CiscoL2L3IfConfigMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBCompliances = _CiscoL2L3IfConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1)
)
_CiscoL2L3IfConfigMIBGroups_ObjectIdentity = ObjectIdentity
ciscoL2L3IfConfigMIBGroups = _CiscoL2L3IfConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2)
)

# Managed Objects groups

ciscoL2L3IfConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)
)
ciscoL2L3IfConfigMIBGroup.setObjects(
      *(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"),
        ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoL2L3IfConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)
)
ciscoL2L3IfConfigMIBCompliance.setObjects(
    ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "ciscoL2L3IfConfigMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2L3-INTERFACE-CONFIG-MIB",
    **{"CL2L3InterfaceMode": CL2L3InterfaceMode,
       "ciscoL2L3IfConfigMIB": ciscoL2L3IfConfigMIB,
       "ciscoL2L3IfConfigMIBObjects": ciscoL2L3IfConfigMIBObjects,
       "cL2L3IfConfig": cL2L3IfConfig,
       "cL2L3IfTable": cL2L3IfTable,
       "cL2L3IfEntry": cL2L3IfEntry,
       "cL2L3IfModeAdmin": cL2L3IfModeAdmin,
       "cL2L3IfModeOper": cL2L3IfModeOper,
       "ciscoL2L3IfConfigMIBConformance": ciscoL2L3IfConfigMIBConformance,
       "ciscoL2L3IfConfigMIBCompliances": ciscoL2L3IfConfigMIBCompliances,
       "ciscoL2L3IfConfigMIBCompliance": ciscoL2L3IfConfigMIBCompliance,
       "ciscoL2L3IfConfigMIBGroups": ciscoL2L3IfConfigMIBGroups,
       "ciscoL2L3IfConfigMIBGroup": ciscoL2L3IfConfigMIBGroup}
)
