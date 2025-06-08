# SNMP MIB module (CISCO-ATM-TRAFFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ATM-TRAFFIC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:07:31 2025
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

(atmTrafficDescrParamEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoAtmTrafficExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11)
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficExtMIB.setRevisions(
        ("2002-08-26 00:00",
         "2001-11-01 00:00",
         "1997-05-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmTrafficExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBObjects = _CiscoAtmTrafficExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1)
)
_CiscoAtmTrafficTypeExt_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficTypeExt = _CiscoAtmTrafficTypeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1)
)
_AtmNoClpNoScrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpNoScrCdvt = _AtmNoClpNoScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNoClpNoScrCdvt.setStatus("deprecated")
_AtmClpScrMbsCdvt_ObjectIdentity = ObjectIdentity
atmClpScrMbsCdvt = _AtmClpScrMbsCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmClpScrMbsCdvt.setStatus("current")
_AtmNoClpScrMbsCdvt_ObjectIdentity = ObjectIdentity
atmNoClpScrMbsCdvt = _AtmNoClpScrMbsCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmNoClpScrMbsCdvt.setStatus("current")
_AtmNoClpMcr_ObjectIdentity = ObjectIdentity
atmNoClpMcr = _AtmNoClpMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmNoClpMcr.setStatus("current")
_AtmNoClpMcrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpMcrCdvt = _AtmNoClpMcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmNoClpMcrCdvt.setStatus("current")
_CiscoAtmTrafficTableExt_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficTableExt = _CiscoAtmTrafficTableExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2)
)
_AtmTrafficDescrParamExtTable_Object = MibTable
atmTrafficDescrParamExtTable = _AtmTrafficDescrParamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamExtTable.setStatus("current")
_AtmTrafficDescrParamExtEntry_Object = MibTableRow
atmTrafficDescrParamExtEntry = _AtmTrafficDescrParamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamExtEntry.setStatus("current")


class _AtmTrafficExplicitServCategory_Type(Integer32):
    """Custom type atmTrafficExplicitServCategory based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbrRt", 2),
          ("vbrNrt", 3),
          ("abr", 4),
          ("ubr", 5),
          ("notDef", 6))
    )


_AtmTrafficExplicitServCategory_Type.__name__ = "Integer32"
_AtmTrafficExplicitServCategory_Object = MibTableColumn
atmTrafficExplicitServCategory = _AtmTrafficExplicitServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1),
    _AtmTrafficExplicitServCategory_Type()
)
atmTrafficExplicitServCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficExplicitServCategory.setStatus("current")


class _AtmTrafficDerivedServCategory_Type(Integer32):
    """Custom type atmTrafficDerivedServCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbrRt", 2),
          ("vbrNrt", 3),
          ("abr", 4),
          ("ubr", 5))
    )


_AtmTrafficDerivedServCategory_Type.__name__ = "Integer32"
_AtmTrafficDerivedServCategory_Object = MibTableColumn
atmTrafficDerivedServCategory = _AtmTrafficDerivedServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2),
    _AtmTrafficDerivedServCategory_Type()
)
atmTrafficDerivedServCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrafficDerivedServCategory.setStatus("current")


class _AtmTrafficDescriptorName_Type(SnmpAdminString):
    """Custom type atmTrafficDescriptorName based on SnmpAdminString"""
    defaultValue = OctetString("")


_AtmTrafficDescriptorName_Type.__name__ = "SnmpAdminString"
_AtmTrafficDescriptorName_Object = MibTableColumn
atmTrafficDescriptorName = _AtmTrafficDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 3),
    _AtmTrafficDescriptorName_Type()
)
atmTrafficDescriptorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescriptorName.setStatus("current")
_CiscoAtmTrafficExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBConformance = _CiscoAtmTrafficExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3)
)
_CiscoAtmTrafficExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBCompliances = _CiscoAtmTrafficExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1)
)
_CiscoAtmTrafficExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBGroups = _CiscoAtmTrafficExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2)
)
atmTrafficDescrParamEntry.registerAugmentions(
    ("CISCO-ATM-TRAFFIC-MIB",
     "atmTrafficDescrParamExtEntry")
)
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())

# Managed Objects groups

ciscoAtmTrafficTableExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1)
)
ciscoAtmTrafficTableExtMIBGroup.setObjects(
      *(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficExplicitServCategory"),
        ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDerivedServCategory"))
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficTableExtMIBGroup.setStatus("current")

ciscoAtmTrafficNmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 2)
)
ciscoAtmTrafficNmsGroup.setObjects(
    ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescriptorName")
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficNmsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmTrafficExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 1)
)
ciscoAtmTrafficExtMIBCompliance.setObjects(
    ("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAtmTrafficExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 2)
)
ciscoAtmTrafficExtMIBComplianceRev1.setObjects(
      *(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"),
        ("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficNmsGroup"))
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-TRAFFIC-MIB",
    **{"ciscoAtmTrafficExtMIB": ciscoAtmTrafficExtMIB,
       "ciscoAtmTrafficExtMIBObjects": ciscoAtmTrafficExtMIBObjects,
       "ciscoAtmTrafficTypeExt": ciscoAtmTrafficTypeExt,
       "atmNoClpNoScrCdvt": atmNoClpNoScrCdvt,
       "atmClpScrMbsCdvt": atmClpScrMbsCdvt,
       "atmNoClpScrMbsCdvt": atmNoClpScrMbsCdvt,
       "atmNoClpMcr": atmNoClpMcr,
       "atmNoClpMcrCdvt": atmNoClpMcrCdvt,
       "ciscoAtmTrafficTableExt": ciscoAtmTrafficTableExt,
       "atmTrafficDescrParamExtTable": atmTrafficDescrParamExtTable,
       "atmTrafficDescrParamExtEntry": atmTrafficDescrParamExtEntry,
       "atmTrafficExplicitServCategory": atmTrafficExplicitServCategory,
       "atmTrafficDerivedServCategory": atmTrafficDerivedServCategory,
       "atmTrafficDescriptorName": atmTrafficDescriptorName,
       "ciscoAtmTrafficExtMIBConformance": ciscoAtmTrafficExtMIBConformance,
       "ciscoAtmTrafficExtMIBCompliances": ciscoAtmTrafficExtMIBCompliances,
       "ciscoAtmTrafficExtMIBCompliance": ciscoAtmTrafficExtMIBCompliance,
       "ciscoAtmTrafficExtMIBComplianceRev1": ciscoAtmTrafficExtMIBComplianceRev1,
       "ciscoAtmTrafficExtMIBGroups": ciscoAtmTrafficExtMIBGroups,
       "ciscoAtmTrafficTableExtMIBGroup": ciscoAtmTrafficTableExtMIBGroup,
       "ciscoAtmTrafficNmsGroup": ciscoAtmTrafficNmsGroup}
)
