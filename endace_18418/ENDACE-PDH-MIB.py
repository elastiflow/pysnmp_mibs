# SNMP MIB module (ENDACE-PDH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/endace_18418/ENDACE-PDH-MIB.mib
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

endacePDHMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 6)
)
if mibBuilder.loadTexts:
    endacePDHMIB.setRevisions(
        ("2007-08-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pdh1_ObjectIdentity = ObjectIdentity
pdh1 = _Pdh1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4)
)
_PdhControlTable_Object = MibTable
pdhControlTable = _PdhControlTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pdhControlTable.setStatus("current")
_PdhControlEntry_Object = MibTableRow
pdhControlEntry = _PdhControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1)
)
pdhControlEntry.setIndexNames(
    (0, "ENDACE-PDH-MIB", "pdhControlIndex"),
)
if mibBuilder.loadTexts:
    pdhControlEntry.setStatus("current")
_PdhControlIndex_Type = InterfaceIndex
_PdhControlIndex_Object = MibTableColumn
pdhControlIndex = _PdhControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 1),
    _PdhControlIndex_Type()
)
pdhControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlIndex.setStatus("current")
_PdhControlAIS_Type = TruthValue
_PdhControlAIS_Object = MibTableColumn
pdhControlAIS = _PdhControlAIS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 2),
    _PdhControlAIS_Type()
)
pdhControlAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlAIS.setStatus("current")
_PdhControlLOF_Type = TruthValue
_PdhControlLOF_Object = MibTableColumn
pdhControlLOF = _PdhControlLOF_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 3),
    _PdhControlLOF_Type()
)
pdhControlLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlLOF.setStatus("current")
_PdhControlLOS_Type = TruthValue
_PdhControlLOS_Object = MibTableColumn
pdhControlLOS = _PdhControlLOS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 4),
    _PdhControlLOS_Type()
)
pdhControlLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlLOS.setStatus("current")
_PdhControlCRCErr_Type = TruthValue
_PdhControlCRCErr_Object = MibTableColumn
pdhControlCRCErr = _PdhControlCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 5),
    _PdhControlCRCErr_Type()
)
pdhControlCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlCRCErr.setStatus("current")
_PdhControlFErr_Type = TruthValue
_PdhControlFErr_Object = MibTableColumn
pdhControlFErr = _PdhControlFErr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 6),
    _PdhControlFErr_Type()
)
pdhControlFErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlFErr.setStatus("current")
_PdhControlLCV_Type = TruthValue
_PdhControlLCV_Object = MibTableColumn
pdhControlLCV = _PdhControlLCV_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 7),
    _PdhControlLCV_Type()
)
pdhControlLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlLCV.setStatus("current")
_PdhControlLink_Type = TruthValue
_PdhControlLink_Object = MibTableColumn
pdhControlLink = _PdhControlLink_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 8),
    _PdhControlLink_Type()
)
pdhControlLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlLink.setStatus("current")
_PdhControlRX0_Type = TruthValue
_PdhControlRX0_Object = MibTableColumn
pdhControlRX0 = _PdhControlRX0_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 9),
    _PdhControlRX0_Type()
)
pdhControlRX0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlRX0.setStatus("current")
_PdhControlRX1_Type = TruthValue
_PdhControlRX1_Object = MibTableColumn
pdhControlRX1 = _PdhControlRX1_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 10),
    _PdhControlRX1_Type()
)
pdhControlRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlRX1.setStatus("current")
_PdhControlRDI_Type = TruthValue
_PdhControlRDI_Object = MibTableColumn
pdhControlRDI = _PdhControlRDI_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 11),
    _PdhControlRDI_Type()
)
pdhControlRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlRDI.setStatus("current")
_PdhControlRLE_Type = TruthValue
_PdhControlRLE_Object = MibTableColumn
pdhControlRLE = _PdhControlRLE_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 4, 1, 1, 12),
    _PdhControlRLE_Type()
)
pdhControlRLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhControlRLE.setStatus("current")
_PdhConformance_ObjectIdentity = ObjectIdentity
pdhConformance = _PdhConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5)
)
_PdhCompliances_ObjectIdentity = ObjectIdentity
pdhCompliances = _PdhCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5, 1)
)
_PdhGroups_ObjectIdentity = ObjectIdentity
pdhGroups = _PdhGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5, 2)
)

# Managed Objects groups

pdhControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5, 2, 1)
)
pdhControlGroup.setObjects(
      *(("ENDACE-PDH-MIB", "pdhControlIndex"),
        ("ENDACE-PDH-MIB", "pdhControlAIS"),
        ("ENDACE-PDH-MIB", "pdhControlLOF"),
        ("ENDACE-PDH-MIB", "pdhControlLOS"))
)
if mibBuilder.loadTexts:
    pdhControlGroup.setStatus("current")

pdhControlGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5, 2, 2)
)
pdhControlGroup2.setObjects(
      *(("ENDACE-PDH-MIB", "pdhControlRLE"),
        ("ENDACE-PDH-MIB", "pdhControlLink"),
        ("ENDACE-PDH-MIB", "pdhControlCRCErr"),
        ("ENDACE-PDH-MIB", "pdhControlFErr"),
        ("ENDACE-PDH-MIB", "pdhControlLCV"),
        ("ENDACE-PDH-MIB", "pdhControlRX0"),
        ("ENDACE-PDH-MIB", "pdhControlRX1"),
        ("ENDACE-PDH-MIB", "pdhControlRDI"))
)
if mibBuilder.loadTexts:
    pdhControlGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdhCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 2, 5, 1, 1)
)
pdhCompliance1.setObjects(
      *(("ENDACE-PDH-MIB", "pdhControlGroup"),
        ("ENDACE-PDH-MIB", "pdhControlGroup2"))
)
if mibBuilder.loadTexts:
    pdhCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-PDH-MIB",
    **{"pdh1": pdh1,
       "pdhControlTable": pdhControlTable,
       "pdhControlEntry": pdhControlEntry,
       "pdhControlIndex": pdhControlIndex,
       "pdhControlAIS": pdhControlAIS,
       "pdhControlLOF": pdhControlLOF,
       "pdhControlLOS": pdhControlLOS,
       "pdhControlCRCErr": pdhControlCRCErr,
       "pdhControlFErr": pdhControlFErr,
       "pdhControlLCV": pdhControlLCV,
       "pdhControlLink": pdhControlLink,
       "pdhControlRX0": pdhControlRX0,
       "pdhControlRX1": pdhControlRX1,
       "pdhControlRDI": pdhControlRDI,
       "pdhControlRLE": pdhControlRLE,
       "pdhConformance": pdhConformance,
       "pdhCompliances": pdhCompliances,
       "pdhCompliance1": pdhCompliance1,
       "pdhGroups": pdhGroups,
       "pdhControlGroup": pdhControlGroup,
       "pdhControlGroup2": pdhControlGroup2,
       "endacePDHMIB": endacePDHMIB}
)
