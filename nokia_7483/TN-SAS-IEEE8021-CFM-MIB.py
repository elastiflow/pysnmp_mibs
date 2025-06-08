# SNMP MIB module (TN-SAS-IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SAS-IEEE8021-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:36 2025
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

(dot1agCfmMepEntry,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMepEntry")

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

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")


# MODULE-IDENTITY

tnSASIEEE8021CfmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tnSASIEEE8021CfmMIBModule.setRevisions(
        ("1910-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSASDot1agMIBObjs_ObjectIdentity = ObjectIdentity
tnSASDot1agMIBObjs = _TnSASDot1agMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11)
)
_TnSASDot1agCfmMep_ObjectIdentity = ObjectIdentity
tnSASDot1agCfmMep = _TnSASDot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1)
)
_TnDot1agCfmMepExtnTable_Object = MibTable
tnDot1agCfmMepExtnTable = _TnDot1agCfmMepExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepExtnTable.setStatus("current")
_TnDot1agCfmMepExtnEntry_Object = MibTableRow
tnDot1agCfmMepExtnEntry = _TnDot1agCfmMepExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepExtnEntry.setStatus("current")


class _TnDot1agCfmMepSendAisOnPortDown_Type(TruthValue):
    """Custom type tnDot1agCfmMepSendAisOnPortDown based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMepSendAisOnPortDown_Type.__name__ = "TruthValue"
_TnDot1agCfmMepSendAisOnPortDown_Object = MibTableColumn
tnDot1agCfmMepSendAisOnPortDown = _TnDot1agCfmMepSendAisOnPortDown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1, 1),
    _TnDot1agCfmMepSendAisOnPortDown_Type()
)
tnDot1agCfmMepSendAisOnPortDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSendAisOnPortDown.setStatus("current")


class _TnDot1agCfmMepControlSapTag_Type(Unsigned32):
    """Custom type tnDot1agCfmMepControlSapTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 768),
    )


_TnDot1agCfmMepControlSapTag_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepControlSapTag_Object = MibTableColumn
tnDot1agCfmMepControlSapTag = _TnDot1agCfmMepControlSapTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1, 2),
    _TnDot1agCfmMepControlSapTag_Type()
)
tnDot1agCfmMepControlSapTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepControlSapTag.setStatus("current")
dot1agCfmMepEntry.registerAugmentions(
    ("TN-SAS-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepExtnEntry")
)
tnDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-IEEE8021-CFM-MIB",
    **{"tnSASIEEE8021CfmMIBModule": tnSASIEEE8021CfmMIBModule,
       "tnSASDot1agMIBObjs": tnSASDot1agMIBObjs,
       "tnSASDot1agCfmMep": tnSASDot1agCfmMep,
       "tnDot1agCfmMepExtnTable": tnDot1agCfmMepExtnTable,
       "tnDot1agCfmMepExtnEntry": tnDot1agCfmMepExtnEntry,
       "tnDot1agCfmMepSendAisOnPortDown": tnDot1agCfmMepSendAisOnPortDown,
       "tnDot1agCfmMepControlSapTag": tnDot1agCfmMepControlSapTag}
)
