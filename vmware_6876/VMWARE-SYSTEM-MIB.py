# SNMP MIB module (VMWARE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vmware_6876/VMWARE-SYSTEM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:23:14 2025
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

(vmwSystem,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwSystem")


# MODULE-IDENTITY

vmwSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10)
)
if mibBuilder.loadTexts:
    vmwSystemMIB.setRevisions(
        ("2010-08-02 00:00",
         "2008-01-12 00:00",
         "2007-12-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwProdName_Type = DisplayString
_VmwProdName_Object = MibScalar
vmwProdName = _VmwProdName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 1),
    _VmwProdName_Type()
)
vmwProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdName.setStatus("current")
_VmwProdVersion_Type = DisplayString
_VmwProdVersion_Object = MibScalar
vmwProdVersion = _VmwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 2),
    _VmwProdVersion_Type()
)
vmwProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdVersion.setStatus("current")
_VmwProdBuild_Type = DisplayString
_VmwProdBuild_Object = MibScalar
vmwProdBuild = _VmwProdBuild_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 4),
    _VmwProdBuild_Type()
)
vmwProdBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdBuild.setStatus("current")
_VmwProdUpdate_Type = DisplayString
_VmwProdUpdate_Object = MibScalar
vmwProdUpdate = _VmwProdUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 5),
    _VmwProdUpdate_Type()
)
vmwProdUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdUpdate.setStatus("current")
_VmwProdPatch_Type = DisplayString
_VmwProdPatch_Object = MibScalar
vmwProdPatch = _VmwProdPatch_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 6),
    _VmwProdPatch_Type()
)
vmwProdPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdPatch.setStatus("current")
_VmwSystemMIBConformance_ObjectIdentity = ObjectIdentity
vmwSystemMIBConformance = _VmwSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2)
)
_VmwSystemMIBCompliances_ObjectIdentity = ObjectIdentity
vmwSystemMIBCompliances = _VmwSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1)
)
_VmwSysMIBGroups_ObjectIdentity = ObjectIdentity
vmwSysMIBGroups = _VmwSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2)
)

# Managed Objects groups

vmwSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2, 1)
)
vmwSystemGroup.setObjects(
      *(("VMWARE-SYSTEM-MIB", "vmwProdName"),
        ("VMWARE-SYSTEM-MIB", "vmwProdVersion"),
        ("VMWARE-SYSTEM-MIB", "vmwProdBuild"),
        ("VMWARE-SYSTEM-MIB", "vmwProdUpdate"),
        ("VMWARE-SYSTEM-MIB", "vmwProdPatch"))
)
if mibBuilder.loadTexts:
    vmwSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vmwSysMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1, 2)
)
vmwSysMIBBasicCompliance.setObjects(
    ("VMWARE-SYSTEM-MIB", "vmwSystemGroup")
)
if mibBuilder.loadTexts:
    vmwSysMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-SYSTEM-MIB",
    **{"vmwProdName": vmwProdName,
       "vmwProdVersion": vmwProdVersion,
       "vmwProdBuild": vmwProdBuild,
       "vmwProdUpdate": vmwProdUpdate,
       "vmwProdPatch": vmwProdPatch,
       "vmwSystemMIB": vmwSystemMIB,
       "vmwSystemMIBConformance": vmwSystemMIBConformance,
       "vmwSystemMIBCompliances": vmwSystemMIBCompliances,
       "vmwSysMIBBasicCompliance": vmwSysMIBBasicCompliance,
       "vmwSysMIBGroups": vmwSysMIBGroups,
       "vmwSystemGroup": vmwSystemGroup}
)
