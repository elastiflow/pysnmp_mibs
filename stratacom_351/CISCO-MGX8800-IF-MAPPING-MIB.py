# SNMP MIB module (CISCO-MGX8800-IF-MAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MGX8800-IF-MAPPING-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:08:16 2025
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoMGX8800IfMappingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7)
)
if mibBuilder.loadTexts:
    ciscoMGX8800IfMappingMIB.setRevisions(
        ("2004-05-25 00:00",
         "2004-04-30 00:00",
         "2003-12-04 00:00",
         "2003-03-20 00:00",
         "2002-10-21 00:00",
         "2002-10-16 00:00",
         "2002-05-21 00:00",
         "2002-02-17 00:00",
         "2001-10-16 00:00",
         "2001-07-08 00:00",
         "2000-02-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmimIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("physicalLine", 1),
          ("atmIma", 2),
          ("atm", 3),
          ("atmVirtual", 4),
          ("ds1Inds3", 5),
          ("adjCardApsLine", 6),
          ("propAtm", 7),
          ("sonetVT", 8),
          ("imaGrpAtmPhy", 9),
          ("srmBertLine", 10),
          ("srmBertPort", 11),
          ("sonetPath", 12),
          ("ds3SonetPath", 13),
          ("atmSonetPath", 14),
          ("atmDs3SonetPath", 15),
          ("frameRelayPort", 16),
          ("ces", 17),
          ("ds1VTPath", 18),
          ("ds1Ds3SonetPath", 19),
          ("atmVciEndPt", 20),
          ("mfrBundle", 21),
          ("ppplink", 22),
          ("pppMpbundle", 23),
          ("lapd", 24))
    )



# MIB Managed Objects in the order of their OIDs

_CmimMappingObjects_ObjectIdentity = ObjectIdentity
cmimMappingObjects = _CmimMappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1)
)
_CmimPhysToIf_ObjectIdentity = ObjectIdentity
cmimPhysToIf = _CmimPhysToIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1)
)
_CmimPhysToIfTable_Object = MibTable
cmimPhysToIfTable = _CmimPhysToIfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmimPhysToIfTable.setStatus("current")
_CmimPhysToIfEntry_Object = MibTableRow
cmimPhysToIfEntry = _CmimPhysToIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1)
)
cmimPhysToIfEntry.setIndexNames(
    (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimModuleIndex"),
    (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfNumber"),
    (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfType"),
)
if mibBuilder.loadTexts:
    cmimPhysToIfEntry.setStatus("current")
_CmimModuleIndex_Type = Unsigned32
_CmimModuleIndex_Object = MibTableColumn
cmimModuleIndex = _CmimModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 1),
    _CmimModuleIndex_Type()
)
cmimModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmimModuleIndex.setStatus("current")
_CmimIfNumber_Type = Unsigned32
_CmimIfNumber_Object = MibTableColumn
cmimIfNumber = _CmimIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 2),
    _CmimIfNumber_Type()
)
cmimIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmimIfNumber.setStatus("current")
_CmimIfType_Type = CmimIfType
_CmimIfType_Object = MibTableColumn
cmimIfType = _CmimIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 3),
    _CmimIfType_Type()
)
cmimIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmimIfType.setStatus("current")
_CmimIfIndex_Type = InterfaceIndex
_CmimIfIndex_Object = MibTableColumn
cmimIfIndex = _CmimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 4),
    _CmimIfIndex_Type()
)
cmimIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmimIfIndex.setStatus("current")
_CmimPhysToIfMIBConformance_ObjectIdentity = ObjectIdentity
cmimPhysToIfMIBConformance = _CmimPhysToIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 3)
)
_CmimPhysToIfMIBCompliances_ObjectIdentity = ObjectIdentity
cmimPhysToIfMIBCompliances = _CmimPhysToIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1)
)
_CmimPhysToIfMIBGroups_ObjectIdentity = ObjectIdentity
cmimPhysToIfMIBGroups = _CmimPhysToIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2)
)

# Managed Objects groups

cmimPhysToIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2, 1)
)
cmimPhysToIfMIBGroup.setObjects(
    ("CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfIndex")
)
if mibBuilder.loadTexts:
    cmimPhysToIfMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmimPhysToIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1, 1)
)
cmimPhysToIfMIBCompliance.setObjects(
    ("CISCO-MGX8800-IF-MAPPING-MIB", "cmimPhysToIfMIBGroup")
)
if mibBuilder.loadTexts:
    cmimPhysToIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX8800-IF-MAPPING-MIB",
    **{"CmimIfType": CmimIfType,
       "ciscoMGX8800IfMappingMIB": ciscoMGX8800IfMappingMIB,
       "cmimMappingObjects": cmimMappingObjects,
       "cmimPhysToIf": cmimPhysToIf,
       "cmimPhysToIfTable": cmimPhysToIfTable,
       "cmimPhysToIfEntry": cmimPhysToIfEntry,
       "cmimModuleIndex": cmimModuleIndex,
       "cmimIfNumber": cmimIfNumber,
       "cmimIfType": cmimIfType,
       "cmimIfIndex": cmimIfIndex,
       "cmimPhysToIfMIBConformance": cmimPhysToIfMIBConformance,
       "cmimPhysToIfMIBCompliances": cmimPhysToIfMIBCompliances,
       "cmimPhysToIfMIBCompliance": cmimPhysToIfMIBCompliance,
       "cmimPhysToIfMIBGroups": cmimPhysToIfMIBGroups,
       "cmimPhysToIfMIBGroup": cmimPhysToIfMIBGroup}
)
