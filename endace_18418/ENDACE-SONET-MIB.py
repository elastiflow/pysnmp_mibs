# SNMP MIB module (ENDACE-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/endace_18418/ENDACE-SONET-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:13:01 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

(InterfaceIndex,
 moduleInterfaces,
 shogunModuleMIB) = mibBuilder.importSymbols(
    "ENDACE-MODULE-MIB",
    "InterfaceIndex",
    "moduleInterfaces",
    "shogunModuleMIB")

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

endaceSONETMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 5)
)
if mibBuilder.loadTexts:
    endaceSONETMIB.setRevisions(
        ("2007-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sonet1_ObjectIdentity = ObjectIdentity
sonet1 = _Sonet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3)
)
_SonetControlTable_Object = MibTable
sonetControlTable = _SonetControlTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sonetControlTable.setStatus("current")
_SonetControlEntry_Object = MibTableRow
sonetControlEntry = _SonetControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1)
)
sonetControlEntry.setIndexNames(
    (0, "ENDACE-SONET-MIB", "sonetControlIndex"),
)
if mibBuilder.loadTexts:
    sonetControlEntry.setStatus("current")
_SonetControlIndex_Type = InterfaceIndex
_SonetControlIndex_Object = MibTableColumn
sonetControlIndex = _SonetControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 1),
    _SonetControlIndex_Type()
)
sonetControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlIndex.setStatus("current")
_SonetControlFault_Type = TruthValue
_SonetControlFault_Object = MibTableColumn
sonetControlFault = _SonetControlFault_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 2),
    _SonetControlFault_Type()
)
sonetControlFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlFault.setStatus("current")
_SonetControlLOF_Type = TruthValue
_SonetControlLOF_Object = MibTableColumn
sonetControlLOF = _SonetControlLOF_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 3),
    _SonetControlLOF_Type()
)
sonetControlLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlLOF.setStatus("current")
_SonetControlLOS_Type = TruthValue
_SonetControlLOS_Object = MibTableColumn
sonetControlLOS = _SonetControlLOS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 4),
    _SonetControlLOS_Type()
)
sonetControlLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlLOS.setStatus("current")
_SonetControlOOF_Type = TruthValue
_SonetControlOOF_Object = MibTableColumn
sonetControlOOF = _SonetControlOOF_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 5),
    _SonetControlOOF_Type()
)
sonetControlOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlOOF.setStatus("current")
_SonetControlLOP_Type = TruthValue
_SonetControlLOP_Object = MibTableColumn
sonetControlLOP = _SonetControlLOP_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 6),
    _SonetControlLOP_Type()
)
sonetControlLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlLOP.setStatus("current")


class _SonetControlCRCSelect_Type(OctetString):
    """Custom type sonetControlCRCSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SonetControlCRCSelect_Type.__name__ = "OctetString"
_SonetControlCRCSelect_Object = MibTableColumn
sonetControlCRCSelect = _SonetControlCRCSelect_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 7),
    _SonetControlCRCSelect_Type()
)
sonetControlCRCSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlCRCSelect.setStatus("current")
_SonetControlPScramble_Type = TruthValue
_SonetControlPScramble_Object = MibTableColumn
sonetControlPScramble = _SonetControlPScramble_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 8),
    _SonetControlPScramble_Type()
)
sonetControlPScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlPScramble.setStatus("current")
_SonetControlRDI_Type = TruthValue
_SonetControlRDI_Object = MibTableColumn
sonetControlRDI = _SonetControlRDI_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 9),
    _SonetControlRDI_Type()
)
sonetControlRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlRDI.setStatus("current")
_SonetControlRAI_Type = TruthValue
_SonetControlRAI_Object = MibTableColumn
sonetControlRAI = _SonetControlRAI_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 10),
    _SonetControlRAI_Type()
)
sonetControlRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlRAI.setStatus("current")
_SonetControlC2_Type = Gauge32
_SonetControlC2_Object = MibTableColumn
sonetControlC2 = _SonetControlC2_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 11),
    _SonetControlC2_Type()
)
sonetControlC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlC2.setStatus("current")
_SonetControlScramble_Type = TruthValue
_SonetControlScramble_Object = MibTableColumn
sonetControlScramble = _SonetControlScramble_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 12),
    _SonetControlScramble_Type()
)
sonetControlScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlScramble.setStatus("current")
_SonetControlAIS_Type = TruthValue
_SonetControlAIS_Object = MibTableColumn
sonetControlAIS = _SonetControlAIS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 13),
    _SonetControlAIS_Type()
)
sonetControlAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlAIS.setStatus("current")
_SonetControlBIP3_Type = TruthValue
_SonetControlBIP3_Object = MibTableColumn
sonetControlBIP3 = _SonetControlBIP3_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 14),
    _SonetControlBIP3_Type()
)
sonetControlBIP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlBIP3.setStatus("current")
_SonetControlREI_Type = TruthValue
_SonetControlREI_Object = MibTableColumn
sonetControlREI = _SonetControlREI_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1, 15),
    _SonetControlREI_Type()
)
sonetControlREI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetControlREI.setStatus("current")
_SonetConformance_ObjectIdentity = ObjectIdentity
sonetConformance = _SonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4)
)
_SonetCompliances_ObjectIdentity = ObjectIdentity
sonetCompliances = _SonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4, 1)
)
_SonetGroups_ObjectIdentity = ObjectIdentity
sonetGroups = _SonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4, 2)
)

# Managed Objects groups

sonetControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4, 2, 1)
)
sonetControlGroup.setObjects(
      *(("ENDACE-SONET-MIB", "sonetControlIndex"),
        ("ENDACE-SONET-MIB", "sonetControlLOF"),
        ("ENDACE-SONET-MIB", "sonetControlLOS"),
        ("ENDACE-SONET-MIB", "sonetControlOOF"),
        ("ENDACE-SONET-MIB", "sonetControlLOP"),
        ("ENDACE-SONET-MIB", "sonetControlCRCSelect"),
        ("ENDACE-SONET-MIB", "sonetControlPScramble"))
)
if mibBuilder.loadTexts:
    sonetControlGroup.setStatus("current")

soneStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4, 2, 2)
)
soneStatusGroup.setObjects(
      *(("ENDACE-SONET-MIB", "sonetControlFault"),
        ("ENDACE-SONET-MIB", "sonetControlRDI"),
        ("ENDACE-SONET-MIB", "sonetControlRAI"),
        ("ENDACE-SONET-MIB", "sonetControlC2"),
        ("ENDACE-SONET-MIB", "sonetControlScramble"),
        ("ENDACE-SONET-MIB", "sonetControlAIS"),
        ("ENDACE-SONET-MIB", "sonetControlBIP3"),
        ("ENDACE-SONET-MIB", "sonetControlREI"))
)
if mibBuilder.loadTexts:
    soneStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sonetCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 2, 4, 1, 1)
)
sonetCompliance1.setObjects(
    ("ENDACE-SONET-MIB", "sonetControlGroup")
)
if mibBuilder.loadTexts:
    sonetCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-SONET-MIB",
    **{"sonet1": sonet1,
       "sonetControlTable": sonetControlTable,
       "sonetControlEntry": sonetControlEntry,
       "sonetControlIndex": sonetControlIndex,
       "sonetControlFault": sonetControlFault,
       "sonetControlLOF": sonetControlLOF,
       "sonetControlLOS": sonetControlLOS,
       "sonetControlOOF": sonetControlOOF,
       "sonetControlLOP": sonetControlLOP,
       "sonetControlCRCSelect": sonetControlCRCSelect,
       "sonetControlPScramble": sonetControlPScramble,
       "sonetControlRDI": sonetControlRDI,
       "sonetControlRAI": sonetControlRAI,
       "sonetControlC2": sonetControlC2,
       "sonetControlScramble": sonetControlScramble,
       "sonetControlAIS": sonetControlAIS,
       "sonetControlBIP3": sonetControlBIP3,
       "sonetControlREI": sonetControlREI,
       "sonetConformance": sonetConformance,
       "sonetCompliances": sonetCompliances,
       "sonetCompliance1": sonetCompliance1,
       "sonetGroups": sonetGroups,
       "sonetControlGroup": sonetControlGroup,
       "soneStatusGroup": soneStatusGroup,
       "endaceSONETMIB": endaceSONETMIB}
)
