# SNMP MIB module (FOUNDRY-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-POE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:48 2025
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

(snAgentSys,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snAgentSys")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snAgentPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    snAgentPoe.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00",
         "2009-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnAgentPoeGbl_ObjectIdentity = ObjectIdentity
snAgentPoeGbl = _SnAgentPoeGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1)
)
_SnAgentPoeGblPowerCapacityTotal_Type = Unsigned32
_SnAgentPoeGblPowerCapacityTotal_Object = MibScalar
snAgentPoeGblPowerCapacityTotal = _SnAgentPoeGblPowerCapacityTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 1),
    _SnAgentPoeGblPowerCapacityTotal_Type()
)
snAgentPoeGblPowerCapacityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeGblPowerCapacityTotal.setStatus("current")
_SnAgentPoeGblPowerCapacityFree_Type = Unsigned32
_SnAgentPoeGblPowerCapacityFree_Object = MibScalar
snAgentPoeGblPowerCapacityFree = _SnAgentPoeGblPowerCapacityFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 2),
    _SnAgentPoeGblPowerCapacityFree_Type()
)
snAgentPoeGblPowerCapacityFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeGblPowerCapacityFree.setStatus("current")
_SnAgentPoeGblPowerAllocationsRequestsHonored_Type = Unsigned32
_SnAgentPoeGblPowerAllocationsRequestsHonored_Object = MibScalar
snAgentPoeGblPowerAllocationsRequestsHonored = _SnAgentPoeGblPowerAllocationsRequestsHonored_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 1, 3),
    _SnAgentPoeGblPowerAllocationsRequestsHonored_Type()
)
snAgentPoeGblPowerAllocationsRequestsHonored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeGblPowerAllocationsRequestsHonored.setStatus("current")
_SnAgentPoePort_ObjectIdentity = ObjectIdentity
snAgentPoePort = _SnAgentPoePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2)
)
_SnAgentPoePortTable_Object = MibTable
snAgentPoePortTable = _SnAgentPoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2)
)
if mibBuilder.loadTexts:
    snAgentPoePortTable.setStatus("current")
_SnAgentPoePortEntry_Object = MibTableRow
snAgentPoePortEntry = _SnAgentPoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1)
)
snAgentPoePortEntry.setIndexNames(
    (0, "FOUNDRY-POE-MIB", "snAgentPoePortNumber"),
)
if mibBuilder.loadTexts:
    snAgentPoePortEntry.setStatus("current")
_SnAgentPoePortNumber_Type = InterfaceIndex
_SnAgentPoePortNumber_Object = MibTableColumn
snAgentPoePortNumber = _SnAgentPoePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 1),
    _SnAgentPoePortNumber_Type()
)
snAgentPoePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoePortNumber.setStatus("current")


class _SnAgentPoePortControl_Type(Integer32):
    """Custom type snAgentPoePortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("enableLegacyDevice", 4))
    )


_SnAgentPoePortControl_Type.__name__ = "Integer32"
_SnAgentPoePortControl_Object = MibTableColumn
snAgentPoePortControl = _SnAgentPoePortControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 2),
    _SnAgentPoePortControl_Type()
)
snAgentPoePortControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgentPoePortControl.setStatus("current")
_SnAgentPoePortWattage_Type = Integer32
_SnAgentPoePortWattage_Object = MibTableColumn
snAgentPoePortWattage = _SnAgentPoePortWattage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 3),
    _SnAgentPoePortWattage_Type()
)
snAgentPoePortWattage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgentPoePortWattage.setStatus("current")
_SnAgentPoePortClass_Type = Integer32
_SnAgentPoePortClass_Object = MibTableColumn
snAgentPoePortClass = _SnAgentPoePortClass_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 4),
    _SnAgentPoePortClass_Type()
)
snAgentPoePortClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgentPoePortClass.setStatus("current")


class _SnAgentPoePortPriority_Type(Integer32):
    """Custom type snAgentPoePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("critical", 1),
          ("high", 2),
          ("low", 3),
          ("medium", 4),
          ("other", 5))
    )


_SnAgentPoePortPriority_Type.__name__ = "Integer32"
_SnAgentPoePortPriority_Object = MibTableColumn
snAgentPoePortPriority = _SnAgentPoePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 5),
    _SnAgentPoePortPriority_Type()
)
snAgentPoePortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgentPoePortPriority.setStatus("current")
_SnAgentPoePortConsumed_Type = Integer32
_SnAgentPoePortConsumed_Object = MibTableColumn
snAgentPoePortConsumed = _SnAgentPoePortConsumed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 6),
    _SnAgentPoePortConsumed_Type()
)
snAgentPoePortConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoePortConsumed.setStatus("current")
_SnAgentPoePortType_Type = DisplayString
_SnAgentPoePortType_Object = MibTableColumn
snAgentPoePortType = _SnAgentPoePortType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 2, 2, 1, 7),
    _SnAgentPoePortType_Type()
)
snAgentPoePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoePortType.setStatus("current")
_SnAgentPoeModule_ObjectIdentity = ObjectIdentity
snAgentPoeModule = _SnAgentPoeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3)
)
_SnAgentPoeModuleTable_Object = MibTable
snAgentPoeModuleTable = _SnAgentPoeModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    snAgentPoeModuleTable.setStatus("current")
_SnAgentPoeModuleEntry_Object = MibTableRow
snAgentPoeModuleEntry = _SnAgentPoeModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1)
)
snAgentPoeModuleEntry.setIndexNames(
    (0, "FOUNDRY-POE-MIB", "snAgentPoeModuleNumber"),
)
if mibBuilder.loadTexts:
    snAgentPoeModuleEntry.setStatus("current")
_SnAgentPoeModuleNumber_Type = Unsigned32
_SnAgentPoeModuleNumber_Object = MibTableColumn
snAgentPoeModuleNumber = _SnAgentPoeModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 1),
    _SnAgentPoeModuleNumber_Type()
)
snAgentPoeModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeModuleNumber.setStatus("current")
_SnAgentPoeModuleBudget_Type = Unsigned32
_SnAgentPoeModuleBudget_Object = MibTableColumn
snAgentPoeModuleBudget = _SnAgentPoeModuleBudget_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 2),
    _SnAgentPoeModuleBudget_Type()
)
snAgentPoeModuleBudget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgentPoeModuleBudget.setStatus("current")


class _SnAgentPoeModuleMaxPDTypeSupport_Type(Integer32):
    """Custom type snAgentPoeModuleMaxPDTypeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot3af", 0),
          ("ieee802dot3at", 1))
    )


_SnAgentPoeModuleMaxPDTypeSupport_Type.__name__ = "Integer32"
_SnAgentPoeModuleMaxPDTypeSupport_Object = MibTableColumn
snAgentPoeModuleMaxPDTypeSupport = _SnAgentPoeModuleMaxPDTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 3, 1, 1, 3),
    _SnAgentPoeModuleMaxPDTypeSupport_Type()
)
snAgentPoeModuleMaxPDTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeModuleMaxPDTypeSupport.setStatus("current")
_SnAgentPoeUnit_ObjectIdentity = ObjectIdentity
snAgentPoeUnit = _SnAgentPoeUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4)
)
_SnAgentPoeUnitTable_Object = MibTable
snAgentPoeUnitTable = _SnAgentPoeUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    snAgentPoeUnitTable.setStatus("current")
_SnAgentPoeUnitEntry_Object = MibTableRow
snAgentPoeUnitEntry = _SnAgentPoeUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1)
)
snAgentPoeUnitEntry.setIndexNames(
    (0, "FOUNDRY-POE-MIB", "snAgentPoeUnitIndex"),
)
if mibBuilder.loadTexts:
    snAgentPoeUnitEntry.setStatus("current")
_SnAgentPoeUnitIndex_Type = Unsigned32
_SnAgentPoeUnitIndex_Object = MibTableColumn
snAgentPoeUnitIndex = _SnAgentPoeUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 1),
    _SnAgentPoeUnitIndex_Type()
)
snAgentPoeUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeUnitIndex.setStatus("current")
_SnAgentPoeUnitPowerCapacityTotal_Type = Unsigned32
_SnAgentPoeUnitPowerCapacityTotal_Object = MibTableColumn
snAgentPoeUnitPowerCapacityTotal = _SnAgentPoeUnitPowerCapacityTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 2),
    _SnAgentPoeUnitPowerCapacityTotal_Type()
)
snAgentPoeUnitPowerCapacityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeUnitPowerCapacityTotal.setStatus("current")
_SnAgentPoeUnitPowerCapacityFree_Type = Unsigned32
_SnAgentPoeUnitPowerCapacityFree_Object = MibTableColumn
snAgentPoeUnitPowerCapacityFree = _SnAgentPoeUnitPowerCapacityFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 3),
    _SnAgentPoeUnitPowerCapacityFree_Type()
)
snAgentPoeUnitPowerCapacityFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeUnitPowerCapacityFree.setStatus("current")
_SnAgentPoeUnitPowerAllocationsRequestsHonored_Type = Unsigned32
_SnAgentPoeUnitPowerAllocationsRequestsHonored_Object = MibTableColumn
snAgentPoeUnitPowerAllocationsRequestsHonored = _SnAgentPoeUnitPowerAllocationsRequestsHonored_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14, 4, 1, 1, 4),
    _SnAgentPoeUnitPowerAllocationsRequestsHonored_Type()
)
snAgentPoeUnitPowerAllocationsRequestsHonored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentPoeUnitPowerAllocationsRequestsHonored.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-POE-MIB",
    **{"snAgentPoe": snAgentPoe,
       "snAgentPoeGbl": snAgentPoeGbl,
       "snAgentPoeGblPowerCapacityTotal": snAgentPoeGblPowerCapacityTotal,
       "snAgentPoeGblPowerCapacityFree": snAgentPoeGblPowerCapacityFree,
       "snAgentPoeGblPowerAllocationsRequestsHonored": snAgentPoeGblPowerAllocationsRequestsHonored,
       "snAgentPoePort": snAgentPoePort,
       "snAgentPoePortTable": snAgentPoePortTable,
       "snAgentPoePortEntry": snAgentPoePortEntry,
       "snAgentPoePortNumber": snAgentPoePortNumber,
       "snAgentPoePortControl": snAgentPoePortControl,
       "snAgentPoePortWattage": snAgentPoePortWattage,
       "snAgentPoePortClass": snAgentPoePortClass,
       "snAgentPoePortPriority": snAgentPoePortPriority,
       "snAgentPoePortConsumed": snAgentPoePortConsumed,
       "snAgentPoePortType": snAgentPoePortType,
       "snAgentPoeModule": snAgentPoeModule,
       "snAgentPoeModuleTable": snAgentPoeModuleTable,
       "snAgentPoeModuleEntry": snAgentPoeModuleEntry,
       "snAgentPoeModuleNumber": snAgentPoeModuleNumber,
       "snAgentPoeModuleBudget": snAgentPoeModuleBudget,
       "snAgentPoeModuleMaxPDTypeSupport": snAgentPoeModuleMaxPDTypeSupport,
       "snAgentPoeUnit": snAgentPoeUnit,
       "snAgentPoeUnitTable": snAgentPoeUnitTable,
       "snAgentPoeUnitEntry": snAgentPoeUnitEntry,
       "snAgentPoeUnitIndex": snAgentPoeUnitIndex,
       "snAgentPoeUnitPowerCapacityTotal": snAgentPoeUnitPowerCapacityTotal,
       "snAgentPoeUnitPowerCapacityFree": snAgentPoeUnitPowerCapacityFree,
       "snAgentPoeUnitPowerAllocationsRequestsHonored": snAgentPoeUnitPowerAllocationsRequestsHonored}
)
